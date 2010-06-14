## not run draw glacial size level
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv,user="postgres",password="postgres",dbname="GGLIS")


data_e <- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\",\"Elevation\",st_x(centroid(the_geom))",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\"='E(c)' or \"Gl_Class\"='E(v)' or \"Gl_Class\"='E(o)'"))
data_m <- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\",\"Elevation\",st_x(centroid(the_geom))",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\"='M(e)' or \"Gl_Class\"='M(l)' or \"Gl_Class\"='M(lg)' or \"Gl_Class\"='M(o)'"))
data_i <- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\",\"Elevation\",st_x(centroid(the_geom))",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\"='I(s)'"))
data_o <- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\",\"Elevation\",st_x(centroid(the_geom))",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\"='O'"))
data_lon <- dbGetQuery(con,statement=paste(
	"select round(st_x(centroid(the_geom))*10),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"group by round(st_x(centroid(the_geom))*10)"))
data_lon_g <- dbGetQuery(con,statement=paste(
	"select round(st_x(centroid(the_geom))*10),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\" <> 'O'",
	"group by round(st_x(centroid(the_geom))*10)"))

data_lon_m <- dbGetQuery(con,statement=paste(
	"select round(st_x(centroid(the_geom))*10),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\" = 'ME'",
	"group by round(st_x(centroid(the_geom))*10)"))

data_ele <- dbGetQuery(con,statement=paste(
	"select round((\"Elevation\")/100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"group by round((\"Elevation\")/100)",
	"order by round((\"Elevation\")/100)"))
data_ele_g <- dbGetQuery(con,statement=paste(
	"select round((\"Elevation\")/100),sum(\"Gl_Area\")",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"Gl_Class\" <> 'O'",
	"group by round((\"Elevation\")/100)",
	"order by round((\"Elevation\")/100)"))
data_danger<- dbGetQuery(con,statement=paste(
	"select gid,\"Gl_Area\",\"Elevation\",st_x(centroid(the_geom))",
	"from \"Nepal_Glacial_Lake_2009_final\"",
	"where \"PDL_Level\" is not null"))

plot(0,0,type="n",col="blue",xlim=c(80,88.5),ylim=c(2300,5800),xlab="Longitude/deg",ylab="Elevation/m")
polygon(c(75,90,90,75),c(5000,5000,4500,4500),col="NA",border="blue",lty=2)
points(data_e[[4]],data_e[[3]],cex=sqrt(data_e[[2]])*2,col=1,pch=16)
points(data_m[[4]],data_m[[3]],cex=sqrt(data_m[[2]])*2,col=2,pch=0)
points(data_i[[4]],data_i[[3]],cex=sqrt(data_i[[2]])*2,col=3,pch=1)
points(data_o[[4]],data_o[[3]],cex=sqrt(data_o[[2]])*2,col=4,pch=2)
points(data_danger[[4]],data_danger[[3]],cex=sqrt(data_danger[[2]])*2,col='yellow',pch=15)
points(data_lon[[1]]/10,data_lon[[2]]*100+2300,type="l",lwd=2,col="black")
##points(data_lon_g[[1]]/10,data_lon_g[[2]]*100+2300,type="l",lwd=2,col="blue")
##points(data_lon_m[[1]]/10,data_lon_m[[2]]*100+2300,type="l",lwd=2,col=2)
points(data_ele[[2]]/10+80,data_ele[[1]]*100,type="l",lwd=2,col="black")
##points(data_ele_g[[2]]/10+80,data_ele_g[[1]]*100,type="l",lwd=2,col="blue")

legend(87,3500,box.lwd=0,cex=0.8,c("Glacial Erosion Lake","Moraine Dammed Lake","Supra-glacial lake","Non-glacial Lake","Potential Dangerous Lake"),col=c(1,2,3,4,2),pch=c(16,0,1,2,15))

## end run