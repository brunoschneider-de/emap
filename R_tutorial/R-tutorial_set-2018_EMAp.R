# EMAp R Tutorial, Sep 2018

# **** ggplot2 - 1a parte ****

library(ggplot2)

# primeiro scatter plot
ggplot(data = mtcars, aes(x = disp, y = mpg)) + geom_point()

# adicionando cores
# ggplot(mtcars, aes(x = disp, y = mpg, colour = cyl)) + geom_point()

# adicionando cores, variável categórica
# ggplot(mtcars, aes(x = disp, y = mpg, colour = as.factor(cyl))) + geom_point()

# ajustando o tamanho dos pontos
# ggplot(mtcars, aes(x = disp, y = mpg, colour = as.factor(cyl), size = wt)) + geom_point()

# exemplo de double encoding
# ggplot(data = mtcars, aes(x = disp, y = mpg, colour = mpg)) + geom_point()


# **** ggplot2 - 2a parte ****

# add smoothed conditional mean and ribbon
# ggplot(mtcars, aes(x = disp, y = mpg, colour = cyl)) + geom_point() 
# ggplot(mtcars, aes(x = disp, y = mpg, colour = cyl)) + geom_point() + geom_smooth()

# add text
# ggplot(mtcars, aes(x = disp, y = mpg, colour = cyl)) + geom_text(aes(label=cyl)) + geom_smooth() 

# histogram
# ggplot(mtcars, aes(x = disp)) + geom_histogram()

# adjust binwidth
# ggplot(mtcars, aes(x = disp)) + geom_histogram(binwidth = 50)

# boxplot
# ggplot(mtcars, aes(x = as.factor(cyl), y = mpg)) + geom_boxplot()

# adjust colour
# ggplot(mtcars, aes(x = as.factor(cyl), y = mpg, fill = as.factor(cyl))) + geom_boxplot()

# overplotting example
# housing <- read.csv("landdata-states.csv")
# p5 <- ggplot(housing, aes(x = Date, y = Home.Value))
# p5 + geom_line(aes(color = State))

# solution: small multiples (ggplot2 Facets)
# p5 + geom_line() + facet_wrap(~State, ncol = 10)
