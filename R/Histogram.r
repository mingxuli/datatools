## not run draw glacial size level
library(RPostgreSQL)
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv,user="postgres",password="welcome",dbname="GLOF")
data <- dbGetQuery(con,"select \"Gl_Area\" from \"Nepal_Glacial_Lake_Sharad_final\"")
data_hist<-hist(data[[1]],nclass=50)
data_hist
counts=data_hist$counts
hist(data[[1]],nclass=50,freq=FALSE,ylim=c(0,20),col="blue",xlab="Area/ sq.km",ylab="Number/n",main="")
## end run