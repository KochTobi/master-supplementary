#!/usr/bin/env Rscript
library(ggplot2)

## nf-core/rnaseq

S3_costs <- '/home/tobias/MasterThesis/rnaseq-comparison/S3-costs.csv'

S3data <- read.csv(file = S3_costs, sep = ',')
ggplot(data=S3data,aes(x=as.factor(number.of.samples), y=S3.costs)) +  
  geom_col() + theme_bw() +
  geom_text(aes(label = round(S3.costs,4)), vjust = 0, size=3.5) +
  labs(y = "S3 costs in USD", x = "Sample size")                                                                                                         

sample_labeller <- c(
  '1' = "SRR4053807 Transcriptome",
  '5' = "5 Transcriptomes"
)


EC2_costs <- '/home/tobias/MasterThesis/rnaseq-comparison/EC2-costs.csv'
EC2data <- read.csv(file = EC2_costs, sep = ',')
ggplot(data=EC2data, aes(x=as.factor(instance.type), y=EC2.costs)) +
geom_col() + theme_bw() + theme(axis.text.x = element_text(angle = -60, hjust = 0)) +
geom_text(aes(label = round(EC2.costs,2)), vjust = 0, size=3.5) + labs(y = "EC2 costs in USD", x = "Instance Type") +
facet_grid(. ~ number.of.samples, scales = "free", space = "free", labeller = as_labeller(sample_labeller))

## SciLifeLab/Sarek
# clean workspace
rm(list = ls())
S3_costs <- '/home/tobias/MasterThesis/sarek-comparisons/S3-costs.csv'
sample_labeller <- function(string, suffix = ' Exome'){
  generated_suffix <- function(string) {
    if( as.numeric(string) > 1) {
      print(as.numeric(string))
      return (paste0(suffix,'s'))
    } else {
      return (suffix)
    }
  }
  paste0(string, lapply(string, generated_suffix))
}
S3data <- read.csv(file = S3_costs, sep = ',')
ggplot(data=S3data,aes(x=as.factor(bucketname), y=S3.costs)) +  
  geom_col() + theme_bw() + theme(axis.text.x = element_text(angle = -60, hjust = 0)) +
  geom_text(aes(label = round(S3.costs,4)), vjust = 0, size=3.5) +
  labs(y = "S3 costs in USD", x = "Sample size")  +
  facet_grid(. ~ number.of.samples, scales = "free", space = "free", labeller = as_labeller(sample_labeller))

EC2_costs <- '/home/tobias/MasterThesis/sarek-comparisons/EC2-costs.csv'

EC2data <- read.csv(file = EC2_costs, sep = ',')
ggplot(data=EC2data, aes(x=as.factor(instance.type), y=EC2.costs)) +
  geom_col() + theme_bw() + theme(axis.text.x = element_text(angle = -60, hjust = 0)) +
  geom_text(aes(label = round(EC2.costs,2)), vjust = 0, size=3.5) + labs(y = "EC2 costs in USD", x = "Instance Type") +
  facet_grid(. ~ number.of.samples, scales = "free", space = "free", labeller = as_labeller(sample_labeller))

