#!/usr/bin/env Rscript
library(ggplot2)

infile <- '~/MasterThesis/rnaseq-comparison/SRR4053807_multiqc.cksum.freq.csv'
outfile <- 'barplot.eps'

cmd_args <- commandArgs(TRUE)
number_of_args = length(cmd_args)


generate_bar <- function(df) {
  figure <- ggplot(data =  df, aes(x = factor(cksum, levels = unique(cksum)), y = count)) +
    geom_bar(stat="identity") + 
    geom_text(aes(label = count), hjust = -1.25, size=3.5) +
    theme_minimal() + 
    coord_flip() +
    labs(y = "Count", x = "Computed Checksum") # coordinate system flipped
  return(figure)
}

if (number_of_args > 0) {
  infile <- cmd_args[1]
  if (number_of_args >= 2) {
    outfile <- cmd_args[2]
  }
} else {
  warning(paste0("No input file given. Defaulting to ",infile))
}

data <- read.csv(infile, header = TRUE, sep = ',')

cairo_ps(filename=paste0(outfile,'.eps'), width = 7, height = 5, pointsize = 12, fallback_resolution = 700)
generate_bar(data)
dev.off()


