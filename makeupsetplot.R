#!/usr/bin/env Rscript
library(UpSetR)

infile <- system.file("extdata", "movies.csv", package="UpSetR")
outfile <- "UpSetR.eps"


remove.na.values <- function(df) {
  df_copy <- cbind(df)
  df_copy <- lapply(df_copy, function(x){x[!is.na(x)]})
  return(df_copy)
}

export.cksum.frequencies <- function(df, filename) {
  df_copy <- cbind(df)
  cksum.list <- unlist(df_copy)
  cksum.table <- table(cksum.list)
  cksum.freqs <- as.data.frame(cksum.table)
  colnames(cksum.freqs) <- c('cksum', 'count')
  # sort dataframe by count
  cksum.freqs.sorted <- cksum.freqs[order(cksum.freqs["count"]),]
  write.table(cksum.freqs.sorted, file = filename, sep = ',', row.names = FALSE)
}

# read the filename
cmd_args <- commandArgs(TRUE)
number_of_args = length(cmd_args)

if (number_of_args > 0) {
  infile <- cmd_args[1]
  if (number_of_args >= 2) {
    outfile <- cmd_args[2]
  } else {
    warning(paste("No location for postscript plot provided. Defaulting to", outfile))
  }
} else {
  stop("No input data available. Please provide a CSV file!")
}
print(paste("Reading CSV file:", infile))
print(paste("Storing plots as:", outfile))

# remove NA values from the columns

data <- read.csv(infile, header = T, sep = ",")
data_trimmed <- remove.na.values(data)

upset_plot <- upset(fromList(data_trimmed), order.by = "degree", nsets = 50)

cairo_ps(filename=paste0(outfile,'.eps'), width = 7, height = 7, pointsize = 12, fallback_resolution = 700)
upset_plot
dev.off()

cairo_pdf(filename=paste0(outfile,'.pdf'), width = 7, height = 7, pointsize = 12, fallback_resolution = 700)
upset_plot
dev.off()

# export chksum frequencies
export.cksum.frequencies(data_trimmed, paste0(outfile,'.cksum.freq.csv'))
