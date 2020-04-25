library(dplyr)
load("D:/gagn3/v3/weight_loss.Rda")

weigh_loss %>% transmute(Individuals, EndResult = Dec - Jan)

weigh_loss %>% transmute(Individuals, WeightRatio = (Dec - Goal) /Jan)

weigh_loss[which.max(weigh_loss$Dec / weigh_loss$Jan), ]

weigh_loss[which.min(weigh_loss$Jan - weigh_loss$Dec), ]

weigh_loss %>% transmute(Individuals, ArangurMarSep = if_else(Feb - Mar > 0 & Aug - Sep > 0, "Gekk vel", "Gekk ekki vel"))

weigh_loss_extended <- weigh_loss %>% mutate(Success_Rate = -(Dec / Jan - 1) * 100)

View(weight_loss_extended)