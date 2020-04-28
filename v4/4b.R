library("readxl")
library("tidyverse")
corona <- read_excel("D:/gagn3/v4/Corona_Virus_Stats.xlsx")

# svo plottid meikar sense
corona[[1]] <- as.Date(corona[[1]], format = "%d-%m-%y")

ggplot(corona, aes(`Reading Taken`, `Total Confirmed`)) + geom_point() +ylim(0, 250000)
