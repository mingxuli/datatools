;-------------------------------------------------------------------------
;+
; NAME:
;   BASE64
;
; PURPOSE:
;   To encrypt/decrypt a byte-array/string using the Base64
;   encryption algorithm
;
; SYNTAX:
;   result = BASE64(array [, /DECRYPT][, /SILENT][, WRITE_TO_FILE=string])
;
; RETURN VALUE:
;   When encrypting, the return value is set to a string array containing
;       the Base64 encrypted data.
;   When decrypting, rhe return value will be a byte array.
;
; ARGUMENTS:
;
;   ARRAY:  When encrypting, ARRAY is set to a 1,2, or 3-dimensional
;       array to be encrypted.
;       When decrypting, ARRAY is set to a 1 or 2-diemsional string
;       array to be decrypted.  Given ARRAY with dimensions MxN, the
;       output will be a M x P x N where P is determined by the length
;       of the input strings.
;
; KEYWORD PARAMETERS:
;
;   DECRYPT: If set, the BASE64 will attempt to decrypt ARRAY.  By default,
;       encryption is performed.  If this keyword is set, ARRAY must be a
;       1 or 2-dimensional string array.
;
;   SILENT: If this keyword is not set, BASE64 will throw helpful messages
;       when encrypting/decrypting.
;
;   WRITE_TO_FILE: Set this keyword (when encrypting) to a string containing
;       the name of a file into which the encrypted data will be written.
;
;
; MODIFICATION HISTORY:
;
;   Jan 2006, Written : Daryl Atencio
;
;-
;-------------------------------------------------------------------------


;-------------------------------------------------------------------------
; CHECK_DATA
;+
;
; Returns whether a variable is of the proper dimensions/type for
; encryption or decryption.
;
;-
Function check_data, data, $
    decrypt = decrypt, $
    data_info = info, $
    outdata = outdata
    
  If N_ELEMENTS(data) Eq 0 Then $
    RETURN, 0
    
  info = SIZE(data)
  
  If info[0] Ne 0 Then $
    If ((WHERE(info[1:info[0]] Eq 1))[0] Eq -1) Then $
    outdata = data $
  Else Begin
  
  outdata = REFORM(data)
  info = SIZE(outdata)
  
Endelse $
Else outdata = data

If KEYWORD_SET(decrypt) Then Begin

  If info[info[0]+1] Ne 7 Then $
    RETURN, 0
    
  If info[0] Gt 2 Then $
    RETURN, 0
    
Endif Else Begin

  If info[info[0]+1] Ne 1 Then $
    RETURN, 0
    
  If info[0] Gt 3 Then $
    RETURN, 0
    
Endelse

RETURN, 1

End



;-------------------------------------------------------------------------
; MAP2ASCII
;+
;
; Converts 6-bit characters to proper Base64 ASCII characters.
; If INVERSE is set MAP2ASCII maps ASCII characters to 6-bit
; characters.
;
;-
Function map2ascii, b, $
    inverse = inverse, $
    padding = pad
    
  If KEYWORD_SET(inverse) Then Begin
    ; Converts base64 characters to corresponding
    ; byte values
  
    bdata = BYTE(b)
    
    ; Get padding (=) information
    w = WHERE(bdata Eq 61b)
    pad = (w[0] Ne -1) ? N_ELEMENTS(w) : 0
    
    ; 0 1 ... 9
    w = WHERE((bdata Ge 48b) And (bdata Le 57b))
    If w[0] Ne -1 Then $
      bdata[w] = bdata[w] + 4b
      
    ; +
    w = WHERE(bdata Eq 43b)
    If w[0] Ne -1 Then $
      bdata[w] = 62b
      
    ; /
    w = WHERE(bdata Eq 47b)
    If w[0] Ne -1 Then $
      bdata[w] = 63b
      
    ; A B ... Z
    w = WHERE((bdata Ge 64b) And (bdata Le 90b))
    If w[0] Ne -1 Then $
      bdata[w] = bdata[w]-65b
      
    ; a b ... z
    w = WHERE((bdata Ge 97b) And (bdata Le 122b))
    If w[0] Ne -1 Then $
      bdata[w] = bdata[w]-71b
      
    RETURN, bdata
    
  Endif Else Begin
    ;
    ; Converts 6-bit characters to proper base64
    ; ASCII characters.
    ;
  
    ; A B ... Z
    w = WHERE((b Ge 0) And (b Le 25))
    If w[0] Ne -1 Then $
      b[w] = b[w] + 65b
      
    ; a b ... z
    w = WHERE((b Ge 26) And (b Le 51))
    If w[0] Ne -1 Then $
      b[w] = b[w] + 71b
      
    ; 0 1 ... 9
    w = WHERE((b Ge 52) And (b Le 61))
    If w[0] Ne -1 Then $
      b[w] = b[w] - 4b
      
    ; +
    w = WHERE(b Eq 62)
    If w[0] Ne -1 Then $
      b[w] = 43b
      
    ; /
    w = WHERE(b Eq 63)
    If w[0] Ne -1 Then $
      b[w] = 47b
      
    ; Padding (=)
    w = WHERE(b Eq 64)
    If w[0] Ne -1 Then Begin
    
      b[w] = 61b
      pad = N_ELEMENTS(w)
      
    Endif Else pad = 0
    
    RETURN, STRING(b)
    
  Endelse
  
End



;-------------------------------------------------------------------------
; BASE64_DECRYPT_LINE
;+
;
; Decrypts a single string.
;
;-
Function base64_decrypt_line, data

  Compile_opt hidden
  
  bdata = map2ascii(data, /inverse, pad = pad)
  
  n = N_ELEMENTS(bdata)
  bdata = REFORM(bdata,4,n/4)
  outdata = BYTARR(3,n/4)
  
  For i = 0, 2 Do Begin
  
    t0 = ISHFT(bdata[i,*],(i+1)*2)
    t1 = ISHFT(bdata[i+1,*], 2*i-4)
    outdata[i,*] = t0 + t1
    
  Endfor
  
  x = 3*n/4
  RETURN, (REFORM(outdata,x))[0:x-pad-1]
  
End



;-------------------------------------------------------------------------
; BASE64_ENCRYPT_LINE
;+
;
; Encrypts a vector of byte values using Base 64 encryption.
;
;-
Function base64_encrypt_line, bdata

  Compile_opt hidden
  
  mask = 63ul
  
  nb = N_ELEMENTS(bdata)
  bdata = REFORM(bdata, nb)
  r = nb Mod 3
  n = CEIL(nb/3.)
  
  b = BYTARR(4,n)
  b[1:3,*] = REVERSE((r Eq 0) ? bdata : [bdata,BYTARR(3-r)])
  
  l = SWAP_ENDIAN(ULONG(b,0,n), /swap_if_big)
  
  For i = 0, 3 Do $
    b[i,*] = ISHFT(l,i*6-26) And mask
    
  If r Gt 0 Then $
    b[r+1:3,0] = 64b
    
  RETURN, map2ascii((n Eq 1) ? b : REFORM(REVERSE(b,2),n*4))
  
End



;-------------------------------------------------------------------------
; BASE64_DECRYPT
;+
;
;   Decrypts a 1 or 2 dimensional array of strings.  A vector of M strings
;   will map to a 2-dimensional byte array with dimensions M x N where N is
;   the number of bytes in a decrypted string.  An M x N 2-dimensional
;   array will map to a M x P x N byte array where P is the number of bytes
;   in a decrypted string.
;
;-
Function base64_decrypt, indata, $
    silent = silent
    
  If ~check_data(indata, /decrypt, $
    data_info = info, outdata = data) Then Begin
    
    If ~KEYWORD_SET(silent) Then $
      MESSAGE, 'Invalid data', /cont
      
    RETURN, -1
    
  Endif
  
  temp = map2ascii(data[0], /inverse, padding = pad)
  n = (N_ELEMENTS(temp) + pad)/4*3 - pad
  
  Case info[0] Of
  
    0: ddata = base64_decrypt_line(data[0])
    
    1: Begin
    
      ddata = BYTARR(n,info[1])
      For i = 0, info[1]-1 Do $
        ddata[*,i] = base64_decrypt_line(data[i])
        
    End
    
    2: Begin
    
      ddata = BYTARR(info[1],n,info[2])
      For i = 0, info[1]-1 Do $
        For j = 0, info[2]-1 Do $
        ddata[i,*,j] = base64_decrypt_line(data[i,j])
        
    End
    
    Else: RETURN, -1
    
  Endcase
  
  RETURN, ddata
  
End



;-------------------------------------------------------------------------
; BASE64_ENCRYPT
;+
;
;   Encrypts a data array using the Base64 encryption algorithm.
;
;-
Function base64_encrypt, indata, $
    write_to_file = filename, $
    silent = silent
    
  If ~check_data(indata, data_info = info, outdata = data) Then Begin
  
    If ~KEYWORD_SET(silent) Then $
      MESSAGE, 'Invalid data', /cont
      
    RETURN, ''
    
  Endif
  
  bytedata = (info[info[0]+1] Eq 7) ? $
    BYTE(data):data
    
  Case info[0] Of
  
    0: edata = base64_encrypt_line(bytedata)
    1: edata = base64_encrypt_line(bytedata)
    2: Begin
    
      edata = STRARR(info[2])
      For i = 0, info[2]-1 Do $
        edata[i] = base64_encrypt_line(bytedata[*,i])
        
    End
    
    ;        3: begin
    ;
    ;            edata = strarr(info[1],info[3])
    ;            for i = 0, info[1]-1 do $
    ;                for j = 0, info[3]-1 do $
    ;                    edata[i,j] = base64_encrypt_line(bytedata[i,*,j])
    3: Begin
    
      edata = STRARR(info[2],info[3])
      For i = 0, info[2]-1 Do $
        For j = 0, info[3]-1 Do $
        edata[i,j] = base64_encrypt_line(bytedata[*,i,j])
        
    End
    
    Else: RETURN, ''
    
  Endcase
  
  ; Write to file
  If N_ELEMENTS(filename) Gt 0 Then Begin
  
    If SIZE(filename, /type) Eq 7 Then Begin
    
      void = 1
      If FILE_TEST(filename[0], /write) Then $
        void = DIALOG_MESSAGE([filename[0] + ' already exists', $
        'Overwrite?'], /quest) Eq 'Yes'
        
      If void Then Begin
      
        OPENW, lun, filename[0], /get_lun
        PRINTF, lun, TRANSPOSE([edata])
        FREE_LUN, lun
        
      Endif
      
    Endif Else $
      MESSAGE, 'Invalid Filename', /cont
      
  Endif
  
  RETURN, edata
  
End



;-------------------------------------------------------------------------
; BASE64
;+
;
; Encrypts/decrypts a byte/string-array, respectively, using Base64
; encryption.
;
;-
Function base64, data, $
    decrypt = decrypt, $
    write_to_file = filename, $
    silent = silent
    
  If KEYWORD_SET(decrypt) Then $
    RETURN, base64_decrypt(data, silent = silent) $
  Else $
    RETURN, base64_encrypt(data, $
    write_to_file = filename, $
    silent = silent)
    
End