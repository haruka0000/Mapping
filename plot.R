data <- read.csv("write.csv")
print(data)

x <- data$x
y <- data$y

plot(x, y, type="l", pch=20, xlim=c(-1000,1000), ylim=c(-1000,1000))
