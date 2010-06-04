## Histogram map of glacial lake type
library("RPostgreSQL")
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv,user="postgres",password="welcome",dbname="GLOF")
total_area<-64.78
data_ec <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='EC'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))
data_ev <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='EV'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_eo <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='EO'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_me <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='ME'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_ml <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='ML'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_mj <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='MJ'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))


data_mo <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='MO'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_is <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='IS'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_iv <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='IV'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_ij <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='IJ'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_io <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='IO'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))

data_o <- dbGetQuery(con,statement=paste(
	"select round(\"Gl_Area\"*100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_Sharad_final\"",
	"where \"Class\"='O'",
	"group by round(\"Gl_Area\"*100)",
	"order by round(\"Gl_Area\"*100)"))


plot(0,0,type="n",xlim=c(0,5),ylim=c(0,5),xlab="Area /sq.km",ylab="Total Area /sq.km")
points(data_ec[[1]]/100,data_ec[[2]],type="p",cex=0.5,col=1,pch=0)
points(data_ev[[1]]/100,data_ev[[2]],type="p",cex=0.5,col=1,pch=1)
points(data_eo[[1]]/100,data_eo[[2]],type="p",cex=0.5,col=1,pch=2)
points(data_me[[1]]/100,data_me[[2]],type="p",cex=0.5,col=2,pch=3)
points(data_ml[[1]]/100,data_ml[[2]],type="p",cex=0.5,col=2,pch=4)
points(data_mj[[1]]/100,data_mj[[2]],type="p",cex=0.5,col=2,pch=5)
points(data_is[[1]]/100,data_is[[2]],type="p",cex=0.5,col=3,pch=6)
points(data_iv[[1]]/100,data_iv[[2]],type="p",cex=0.5,col=3,pch=7)
points(data_ij[[1]]/100,data_ij[[2]],type="p",cex=0.5,col=3,pch=8)
points(data_io[[1]]/100,data_io[[2]],type="p",cex=0.5,col=3,pch=9)
points(data_o[[1]]/100,data_o[[2]],type="p",cex=0.5,col=4,pch=10)
