library(stats)

## part 1 
# utilities:
# x1: Fixed - charge covering ration (income/debt)
# x2: Rate of return on capital
# x3: Cost per KW capacity in place
# x4: Annual Load Factor
# x5: Peak KWH demand growth from 1974 to 1975
# x6: Sales (KWH use per year)
# x7: Percent Nuclear
# x8: Total fuel costs (cents per KWH)

# load and preprocess data
utilities.df <- read.csv("Utilities.csv")
row.names(utilities.df) <- utilities.df[,1]
utilities.df <- utilities.df[,-1]

# normalize data
utilities.df.norm <- sapply(utilities.df, scale)
row.names(utilities.df.norm) <- row.names(utilities.df)

# compute normalized distance based on all 8 variables 
d.norm <- dist(utilities.df.norm,  method = "euclidean")

# in hclust() set argument method = 
# to "ward.D", "single", "complete", "average", "median", or "centroid"

hc1 <- hclust(d.norm, method = "complete")
plot(hc1, hang = -1, ann = FALSE)



memb <- cutree(hc1, k = 6) 
memb

# set labels as cluster membership and utility name
row.names(utilities.df.norm) <- paste(memb, ": ", row.names(utilities.df), sep = "")

# plot heatmaphttp://127.0.0.1:41987/graphics/plot_zoom_png?width=1200&height=900
# rev() reverses the color mapping to large = dark
heatmap(as.matrix(utilities.df.norm), Colv = NA, hclustfun = hclust, col = rev(paste("gray", 1:99, sep = "")))

# run kmeans algorithm
# if you don't set seed every time you run it you would get a different result 
# with the same data (for reproducibility)
set.seed(2) 
km <- kmeans(utilities.df.norm, 3) 

# show cluster membership
km$cluster

# centroids
km$centers

# plot in a scatter plot
plot(c(0), xaxt = 'n', ylab = "", type = "l", ylim = c(min(km$centers), max(km$centers)), xlim = c(0,8))

# label x-axes
axis(1, at = c(1:8), labels = names(utilities.df))

# plot centroids
for (i in c(1:3))
  lines(km$centers[i,], lty = i, lwd = 2, col = ifelse(i%in% c(1,3,5), "black", "dark grey"))

# name clusters
text(x = 0.5, y = km$centers[,1], labels = paste("Cluster", c(1:3)))

## part 2
# p2 congress votes: 
# handicapped-infants: 2 (y,n)
# water-project-cost-sharing: 2 (y,n)
# adoption-of-the-budget-resolution: 2 (y,n)
# physician-fee-freeze: 2 (y,n)
# el-salvador-aid: 2 (y,n)
# religious-groups-in-schools: 2 (y,n)
# anti-satellite-test-ban: 2 (y,n)
# aid-to-nicaraguan-contras: 2 (y,n)
# mx-missile: 2 (y,n)
# immigration: 2 (y,n)
# synfuels-corporation-cutback: 2 (y,n)
# education-spending: 2 (y,n)
# superfund-right-to-sue: 2 (y,n)
# crime: 2 (y,n)
# duty-free-exports: 2 (y,n)
# export-administration-act-south-africa: 2 (y,n)

# p2 congress party affiliations:
# indicates republican or democrat of the 435 congress members of 1984

# load and preprocess data
votes.df <- read.csv("p2_congress_1984_votes.csv")
party.df <- read.csv("p2_congress_1984_party_affiliations.csv")

# sets rownames in votes to which party they belonged to and which number they are represented by
rownames(votes.df) <- paste(party.df[seq(nrow(votes.df)),1], seq(nrow(votes.df)))


# normalize data
votes.df.norm <- sapply(votes.df, scale)
row.names(votes.df.norm) <- row.names(votes.df)

# compute normalized distance based on all 8 variables 
d.norm <- dist(votes.df.norm,  method = "euclidean")


# apply k means (k = 2) 

# run kmeans algorithm
# if you don't set seed every time you run it you would get a different result 
# with the same data (for reproducibility)
set.seed(2) 
km2 <- kmeans(votes.df.norm, 2) 

# show cluster membership
km2$cluster

# centroids
km2$centers

# plot in a scatter plot
plot(c(0), xaxt = 'n', ylab = "", type = "l", ylim = c(min(km2$centers), max(km2$centers)), xlim = c(0,16))

# label x-axes
axis(1, at = c(1:16), labels = names(votes.df))

# plot centroids
for (i in c(1:2))
  lines(km2$centers[i,], lty = i, lwd = 2, col = ifelse(i%in% c(1,3,5,7,9,11,13,15), "black", "dark grey"))

# name clusters
text(x = 0.5, y = km2$centers[,1], labels = paste("Cluster", c(1:2)))

# cluster 1 numbers
one <- votes.df.norm[km2$cluster==1,]

d1 <- 0
r1 <- 0

for (i in c(1:202))
{
  t = substr(row.names(votes.df), 1, 1)
  if (t[i] == "D")
  {
    d1 <- d1 + 1
  }else{ 
    r1 <- r1 + 1
  }
}

print(d1)
print(r1)


# cluster 2 numbers
two <- votes.df.norm[km2$cluster==2,]

d2 <- 0
r2 <- 0

for (i in c(1:232))
{
  t = substr(row.names(votes.df), 1, 1)
  if (t[i] == "D")
  {
    d2 <- d2 + 1
  }else{ 
    r2 <- r2 + 1
  }
}

print(d2)
print(r2)
