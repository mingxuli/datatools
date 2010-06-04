## not run draw glacial size level
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv,user="postgres",password="welcome",dbname="GLOF")
data <- dbGetQuery(con,"select gid,\"Gl_Area\" from \"Nepal_Glacial_Lake_Sharad_final\"")
print(mode(data))
print(data)
print("====end====")
## end run