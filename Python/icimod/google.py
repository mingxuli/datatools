##goolge
import win32com.client,time
ge=win32com.client.Dispach("GoogleEarth.ApplicationGE")
while not googleEarth.IsInitialized():
    time.sleep(0.5)
    print 'wait for Google Earth to initialize'
latitude=41.4879
longitude=-81.6865
altitude=1000
tilt=0
azimuth=370
speed=0.5
range=0
altMod=1
ge.SetCameraParams(latitude,longitude,altitude,altMod,tilt,azimuth,speed)

