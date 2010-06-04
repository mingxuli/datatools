## not run draw glacial size level
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv,user="postgres",password="welcome",dbname="GLOF")
data <- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\"",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Gl_Area\">0.05 and \"Gl_Area\"<0.5"))
hist(data[[2]],50,col="blue",main="",xlab="Area of Glacial Lake/sq.km")

print("====end====")
## end run