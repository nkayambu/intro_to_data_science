# For more details on this exercise, see https://cran.r-project.org/web/packages/tuber/vignettes/tuber-ex.html. 
# For more information on the tuber package, see https://cran.r-project.org/web/packages/tuber/tuber.pdf 

# Install devtools package if not installed already
install.packages('devtools')
# Load devtools package
library(devtools)

# Using devtools to install tuber package from Github
devtools::install_github("soodoku/tuber")#, build_vignettes = TRUE)
# Load tuber package
library(tuber)

# Set working directory. 
setwd("E:/OneDrive - The University of Texas-Rio Grande Valley/Courses/CSCI4344/R/Youtube")

# Authenticate using your YouTube client ID and client secret key
## Then authenticate in browser
client_id="631238115512-tce4bn50n6gojf3hu780bvm4fgcjabgl.apps.googleusercontent.com" # Enter within double quotes your own client ID
client_secret="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"  # Enter within double quotes your own client secret key
yt_oauth(client_id, client_secret, token='')

###############################################################################################################
# Collect data on a Youtube video
###############################################################################################################

# Get statistics of a video with ID 9IIgH0hNtgk. The video ID is the string at the end of the youtube link: https://www.youtube.com/watch?v=9IIgH0hNtgk
get_stats(video_id="nOj_A3aZxGs")

# Get details about the video
get_video_details(video_id="nOj_A3aZxGs")

# Search Videos and save results in data frame called search_result
search_result <- yt_search("Data Analytics")
# Views the first three columns and the first few rows in results
View(search_result)

# Get comments on video and saves them to data frame called comments
comments <- get_comment_threads(c(video_id="nOj_A3aZxGs"))
# View first few rows of comments
View(comments)

# Save comments to a csv file in working directory
write.csv(comments, file='YouTubeVideoComments.csv')

###########################################################################################################
# Create word cloud of the comments
###########################################################################################################

# Install tm, SnowballC and wordcloud packages for text preprocessing and word clods
install.packages('tm')
library(tm)
install.packages('SnowballC')
library(SnowballC)
install.packages('wordcloud')
library(wordcloud)


# Create comments corpus. Corpus is the set of all documnets we want to analyze
comments_corp=Corpus(VectorSource(comments$textOriginal))

# Text processing and create document-term matrix in which rows are documents/comments and coloums are the terms/words
# This function remove the puctuation, numbers and stopwords such as the, a , ...
comments_DTM=DocumentTermMatrix(comments_corp,control=list(removePunctuation=T,removeNumbers=T,stopwords=T))

# Displays first five terms in DTM
as.matrix(comments_DTM[,1:5])

# Create matrix of terms and frequency
comments_terms=colSums(as.matrix(comments_DTM))
comments_terms_matrix=as.matrix(comments_terms)
comments_terms_matrix

# Create word cloud of comments
wordcloud(words=names(comments_terms), freq=comments_terms, vfont=c('serif', 'bold italic'), colors=1:nrow(comments_terms_matrix))

