# Command line log

## nf-core/rnaseq

### AWS

#### **SRR4053807**:

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads s3://eu-west-1-tkoch-rnaseq-data/*.fastq.gz --genome GRCh37 -profile awsbatch -s kochtobi/rnaseq -r awstest -ansi -work-dir s3://eu-west-1-tkoch-rnaseq/work --outdir s3://eu-west-1-tkoch-rnaseq/results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq -resume
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r awstest -profile awsbatch --genome GRCh37 --tracedir tracedir -c readPaths.config --singleEnd -ansi -work-dir s3://eu-west-1-tkoch-rnaseq/work --outdir s3://eu-west-1-tkoch-rnaseq/results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq -resume
```

#### **5 samples:**

##### SampleIDs
* SRR4053795
* SRR4053796
* SRR4053797
* SRR4053798
* SRR4053807

```bash
!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads s3://eu-west-1-tkoch-rnaseq-data/*.fastq.gz --genome GRCh37 -profile awsbatch -s kochtobi/rnaseq -r awstest -ansi -work-dir s3://eu-west-1-tkoch-rnaseq/5samples/work --outdir s3://eu-west-1-tkoch-rnaseq/5samples/results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq-5samples --tracedir tracedir
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r awstest -profile awsbatch --genome GRCh37 --tracedir tracedir -c readPaths.config --singleEnd -ansi -work-dir s3://eu-west-1-tkoch-rnaseq/5samples/work --outdir s3://eu-west-1-tkoch-rnaseq/5samples/results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq-5samples
```

### CFC

#### **SRR4053807 Singularity** 

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "/home-link/zxmqi32/rnaseq-data/\*.fastq.gz" --genome GRCh37 -profile cfc -s kochtobi/rnaseq -r cfctest -ansi
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r cfctest --reads "/home-link/zxmqi32/rnaseq-data/\*.fastq.gz" -profile cfc --genome GRCh37 --singleEnd -ansi
```

#### **SRR4053807 Conda** 

```bash
!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "/home-link/zxmqi32/rnaseq-data/\*.fastq.gz" --genome GRCh37 -profile cfc,noContainers -s kochtobi/rnaseq -r cfctest -ansi
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r cfctest -profile cfc,noContainers --genome GRCh37 --tracedir tracedir --reads "/home-link/zxmqi32/rnaseq-data/\*.fastq.gz" --singleEnd -ansi
```



#### **Singularity all samples**

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "~/RAW_DATA2/RAW_DATA2/\*.fastq" --genome GRCh37 -profile cfc -s /home-link/zxmqi32/rnaseq -ansi -resume
nextflow -log tracedir/.nextflow.log run /home-link/zxmqi32/rnaseq --reads "~/RAW_DATA2/RAW_DATA2/\*.fastq" -profile cfc --genome GRCh37 --singleEnd -ansi -resume
```



#### **Conda all samples** 

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "~/RAW_DATA2/RAW_DATA2/\*.fastq" --genome GRCh37 -profile cfc,noContainers -s /home-link/zxmqi32/rnaseq -ansi
nextflow -log tracedir/.nextflow.log run /home-link/zxmqi32/rnaseq --reads "~/RAW_DATA2/RAW_DATA2/\*.fastq" -profile cfc,noContainers --genome GRCh37 --singleEnd -ansi
```



### Thanos

#### **SRR4053807 Singularity**

```bash
!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "~/rnaseq-data/\*.fastq.gz" --genome GRCh37 -profile thanos,singularity -s kochtobi/rnaseq -r thanostest -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r thanostest -profile thanos,singularity --genome GRCh37 --tracedir tracedir --reads "~/rnaseq-data/\*.fastq.gz" --singleEnd -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq

```

#### **Singularity all samples**

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "~/rnaseq-data/\*.fastq.gz" --genome GRCh37 -profile thanos,singularity -s kochtobi/rnaseq -r thanostest -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r thanostest -profile thanos,singularity --genome GRCh37 --tracedir tracedir --reads "~/rnaseq-data/\*.fastq.gz" --singleEnd -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq
```



#### **Conda all samples**

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/rnaseq-wrapper.py --singleEnd --reads "~/rnaseq-data/\*.fastq.gz" --genome GRCh37 -profile thanos,conda -s kochtobi/rnaseq -r thanostest -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq
nextflow -log tracedir/.nextflow.log run kochtobi/rnaseq -r thanostest -profile thanos,conda --genome GRCh37 --tracedir tracedir --reads "~/rnaseq-data/\*.fastq.gz" --singleEnd -ansi -work-dir work --outdir results --awsregion eu-west-1 --awsqueue tkoch-nfcore-rnaseq
```





## Sarek

### AWS 

#### 1 sample

*nf-test-scripts*

```bash
commit f093c5cc2de3cbc0ff112f6dc911e309bb0f7dd9 (HEAD -> sarek, origin/sarek)
Author: Tobias <tobias.koch@student.uni-tuebingen.de>
Date:   Thu Mar 14 13:51:09 2019 +0100

    fix typo
```



*main.nf* - 2019-02-18-11-57-QXXJH332A3

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-main -aq_germ tkoch-sarek-germline-exome -o s3://tkoch-sarek-out/exomes -w s3://tkoch-sarek-out/exomes --reports exomes_report --script_location /home/ec2-user/Sarek/ -s s3://tkoch-sarek-test/Exomes/QXXJH332A3.tsv
nextflow run /home/ec2-user/Sarek/main.nf -profile awsbatch --awsqueue tkoch-sarek-main --sample s3://tkoch-sarek-test/Exomes/QXXJH332A3.tsv --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://tkoch-sarek-out/exomes/QXXJH332A3/results -w s3://tkoch-sarek-out/exomes/QXXJH332A3/work --localReportDir exomes_report_main -with-report -with-trace -with-timeline -with-dag -ansi
```



*germlineVC.nf* - 2019-02-18-14-8

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-main -aq_germ tkoch-sarek-germline-exome -o s3://tkoch-sarek-out/exomes -w s3://tkoch-sarek-out/exomes --reports exomes_report --script_location /home/ec2-user/Sarek/ -s s3://tkoch-sarek-test/Exomes/QXXJH332A3.tsv
nextflow run /home/ec2-user/Sarek/germlineVC.nf -profile awsbatch --awsqueue tkoch-sarek-germline-exome --tools HaplotypeCaller,strelka,mutect2 --sample s3://tkoch-sarek-out/exomes/QXXJH332A3/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://tkoch-sarek-out/exomes/QXXJH332A3/results -w s3://tkoch-sarek-out/exomes/QXXJH332A3/work --localReportDir exomes_report_germlineVC -with-report -with-trace -with-timeline -with-dag -ansi
```



*annotate.nf* - 2019-02-20-8-33

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-main -aq_germ tkoch-sarek-germline-exome -aq_an tkoch-sarek-annotate -o s3://tkoch-sarek-out/exomes -w s3://tkoch-sarek-out/exomes --reports exomes_report --script_location /home/ec2-user/Sarek/ -s s3://tkoch-sarek-test/Exomes/QXXJH332A3.tsv
nextflow -log exomes_report_annotate/.nextflow.log run /home/ec2-user/Sarek/annotate.nf -profile awsbatch --awsqueue tkoch-sarek-annotate --annotateTools HaplotypeCaller,Strelka --tools snpeff,VEP --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://tkoch-sarek-out/exomes/QXXJH332A3/results -w s3://tkoch-sarek-out/exomes/QXXJH332A3/work --localReportDir exomes_report_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```



#### 2 samples

*nf-test-scripts*

```bash
commit c7986b3eccbf5812a12631f3b9b6f8bc95f58d24 (HEAD -> sarek, origin/sarek)
Author: Tobias <tobias.koch@student.uni-tuebingen.de>
Date:   Mon Apr 22 15:24:38 2019 +0200
```

*main.nf* - 2019-05-18-16-5

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-2exomes-main -aq_germ tkoch-sarek-2exomes_germ -aq_an tkoch-sarek-2exomes-annotate -aq_mqc tkoch-nocpus -o s3://us-east-1-tkoch-sarek-2exomes-out -w s3://us-east-1-tkoch-sarek-2exomes-work --script_location KochTobi/Sarek/ -rev awstesting -s s3://tkoch-sarek-test/aws-2exomes.tsv --steps main germlineVC annotate --profile awsbatch --genome GRCh37
nextflow -log Reports/aws-2exomes_main/.main.nextflow.log run KochTobi/Sarek/main.nf -r awstesting -profile awsbatch --awsqueue tkoch-sarek-2exomes-main --sample s3://tkoch-sarek-test/aws-2exomes.tsv --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://us-east-1-tkoch-sarek-2exomes-out/aws-2exomes/results -w s3://us-east-1-tkoch-sarek-2exomes-work/aws-2exomes/work "" --localReportDir Reports/aws-2exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```

#### 10 samples

*nf-test-scripts*

```bash
commit 3c5116b972c0fdcc48335e90a5a3be54173f9558 (HEAD -> sarek, origin/sarek)
Author: Tobias <tobias.koch@student.uni-tuebingen.de>
Date:   Mon Apr 22 13:35:15 2019 +0200

    add exception handling
```



*main.nf* - 2019-04-22-13-32

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-10exomes-main -aq_germ tkoch-sarek-10exomes-germlineVC -aq_an tkoch-sarek-10exomes-annotate -aq_mqc tkoch-sarek-10exomes-runMultiQC -o s3://us-east-1-tkoch-sarek-10exomes-out -w s3://us-east-1-tkoch-sarek-10exomes-work --script_location KochTobi/Sarek/ -rev awstesting -s s3://tkoch-sarek-test/aws-10exomes.tsv --steps main germlineVC annotate --profile awsbatch --genome GRCh37
nextflow -log Reports/aws-10exomes_main/.main.nextflow.log run KochTobi/Sarek/main.nf -r awstesting -profile awsbatch --awsqueue tkoch-sarek-10exomes-main --sample s3://tkoch-sarek-test/aws-10exomes.tsv --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://us-east-1-tkoch-sarek-10exomes-out/aws-10exomes/results -w s3://us-east-1-tkoch-sarek-10exomes-work/aws-10exomes/work "" --localReportDir Reports/aws-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```

*germlineVC.nf* - 2019-04-22-19-41

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-10exomes-main -aq_germ tkoch-sarek-10exomes-germlineVC -aq_an tkoch-sarek-10exomes-annotate -aq_mqc tkoch-sarek-10exomes-runMultiQC -o s3://us-east-1-tkoch-sarek-10exomes-out -w s3://us-east-1-tkoch-sarek-10exomes-work --script_location KochTobi/Sarek/ -rev awstesting -s s3://tkoch-sarek-test/aws-10exomes.tsv --steps germlineVC --profile awsbatch --genome GRCh37 --resume
nextflow -log Reports/aws-10exomes_germlineVC/.germlineVC.nextflow.log run KochTobi/Sarek/germlineVC.nf -r awstesting -profile awsbatch --awsqueue tkoch-sarek-10exomes-germlineVC --tools HaplotypeCaller,strelka,mutect2 --sample s3://us-east-1-tkoch-sarek-10exomes-out/aws-10exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://us-east-1-tkoch-sarek-10exomes-out/aws-10exomes/results -w s3://us-east-1-tkoch-sarek-10exomes-work/aws-10exomes/work "" --localReportDir Reports/aws-10exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```

*annotate.nf* - 2019-04-22-19-17

```bash
#!/usr/bin/env bash
# python /home/ec2-user/nf-test-scripts/sarek-wrapper.py -aq_main tkoch-sarek-10exomes-main -aq_germ tkoch-sarek-10exomes-germlineVC -aq_an tkoch-sarek-10exomes-annotate -aq_mqc tkoch-sarek-10exomes-runMultiQC -o s3://us-east-1-tkoch-sarek-10exomes-out -w s3://us-east-1-tkoch-sarek-10exomes-work --script_location KochTobi/Sarek/ -rev awstesting -s s3://tkoch-sarek-test/aws-10exomes.tsv --steps germlineVC annotate --profile awsbatch --genome GRCh37
nextflow -log Reports/aws-10exomes_annotate/.annotate.nextflow.log run KochTobi/Sarek/annotate.nf -r awstesting -profile awsbatch --awsqueue tkoch-sarek-10exomes-annotate --annotateTools HaplotypeCaller,Strelka --tools snpeff --genome_base s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir s3://us-east-1-tkoch-sarek-10exomes-out/aws-10exomes/results -w s3://us-east-1-tkoch-sarek-10exomes-work/aws-10exomes/work "" --localReportDir Reports/aws-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```



### CFC

#### **10 samples singularity**

*main.nf* - 2019-03-05-10-49

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv -o . -w . --steps main germlineVC annotate --profile cfc --reports . --script_location /home-link/zxmqi32/Sarek --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 -r
nextflow -log ./cfc-10exomes_main/.main.nextflow.log run /home-link/zxmqi32/Sarek/main.nf -profile cfc --awsqueue none --sample /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work "" --localReportDir ./cfc-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



*germlineVC.nf* - 2019-03-05-15-38

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv -o . -w . --steps main germlineVC annotate --profile cfc --reports . --script_location /home-link/zxmqi32/Sarek --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 -r
nextflow -log ./cfc-10exomes_germlineVC/.nextflow.log run /home-link/zxmqi32/Sarek/germlineVC.nf -profile cfc --awsqueue none --tools HaplotypeCaller,strelka,mutect2 --sample ./cfc-10exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work "" --localReportDir ./cfc-10exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume

```



*annotate.nf* - 2019-03-06-2-26

```bash 
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv -o . -w . --steps germlineVC annotate --profile cfc noContainers --reports . --script_location /home-link/zxmqi32/Sarek --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 -r
nextflow -log ./cfc-10exomes_annotate/.annotate.nextflow.log run /home-link/zxmqi32/Sarek/annotate.nf -profile cfc,noContainers --awsqueue none --annotateTools HaplotypeCaller,Strelka --tools snpeff --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work "" --localReportDir ./cfc-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



#### 10 samples conda

*main.nf* - 2019-03-12-12-46

```bash
nextflow -log ./cfc-10exomes_main/.main.nextflow.log run /home-link/zxmqi32/Sarek/main.nf -profile conda,cfc,noContainers --awsqueue none --sample /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work  --localReportDir ./cfc-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```



*main.nf* - 2019-03-12-14-41

```bash
#!/usr/bin/env nextflow
/home-link/zxmqi32/.local/bin/nextflow -log ./cfc-10exomes_main/.main.nextflow.log run /home-link/zxmqi32/Sarek/main.nf -profile cfc,noContainers --awsqueue none --sample /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work  --localReportDir ./cfc-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



*germlineVC.nf* - 2019-03-13-19-11

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv -o . -w . --steps germlineVC annotate --profile cfc noContainers --reports . --script_location /home-link/zxmqi32/Sarek --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 -r
nextflow -log ./cfc-10exomes_germlineVC/.germlineVC.nextflow.log run /home-link/zxmqi32/Sarek/germlineVC.nf -profile cfc,noContainers --awsqueue none --tools HaplotypeCaller,strelka,mutect2 --sample ./cfc-10exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work "" --localReportDir ./cfc-10exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



*annotate.nf* - 2019-03-14-10-22

```bash
nextflow -log ./cfc-10exomes_annotate/.annotate.nextflow.log run /home-link/zxmqi32/Sarek/annotate.nf -profile cfc,noContainers --awsqueue none --annotateTools HaplotypeCaller,Strelka --tools snpeff --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work --localReportDir ./cfc-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



*annotate.nf* - 2019-03-14-12-52

```bash
#!/usr/bin/env bash
# python /home-link/zxmqi32/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home-link/zxmqi32/nf-test-scripts/cfc-10exomes.tsv -o . -w . --steps annotate --profile cfc noContainers --reports . --script_location /home-link/zxmqi32/Sarek --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 -r
nextflow -log ./cfc-10exomes_annotate/.annotate.nextflow.log run /home-link/zxmqi32/Sarek/annotate.nf -profile cfc,noContainers --awsqueue none --annotateTools HaplotypeCaller,Strelka --tools snpeff --genome_base /home-link/zxmqi32/Reference_Genomes/Human/GRCH37 --genome GRCh37 --outDir ./cfc-10exomes/results -w ./cfc-10exomes/work "" --localReportDir ./cfc-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```





### Thanos

#### QXXJH332A3 conda

*main.nf* - 2019-03-14-16-1

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-exomes.tsv -o . -w . --steps main annotate multiQC --profile conda thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 -r
nextflow -log ./thanos-exomes_main/.main.nextflow.log run /home/tkoch/Sarek/main.nf -profile conda,thanos,noContainers --awsqueue none --sample ./thanos-exomes.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 --outDir ./thanos-exomes/results -w ./thanos-exomes/work "" --localReportDir ./thanos-exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```

*germlineVC.nf* - 2019-03-13-20-31

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-exomes.tsv -o . -w . --steps germlineVC annotate --profile conda thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 -r
nextflow -log ./thanos-exomes_germlineVC/.germlineVC.nextflow.log run /home/tkoch/Sarek/germlineVC.nf -profile conda,thanos,noContainers --awsqueue none --tools HaplotypeCaller,strelka,mutect2 --sample ./thanos-exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 --outDir ./thanos-exomes/results -w ./thanos-exomes/work "" --localReportDir ./thanos-exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```

*annotate.nf* - 2019-03-14-16-5

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-exomes.tsv -o . -w . --steps annotate multiQC --profile conda thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 -r
nextflow -log ./thanos-exomes_annotate/.annotate.nextflow.log run /home/tkoch/Sarek/annotate.nf -profile conda,thanos,noContainers --awsqueue none --annotateTools HaplotypeCaller,Strelka --tools snpeff --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37/ --genome GRCh37 --outDir ./thanos-exomes/results -w ./thanos-exomes/work "" --localReportDir ./thanos-exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```



#### 10 samples

*main.nf* - 2019-03-18-16-29

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home/tkoch/sarek-10exomes/thanos-10exomes.tsv -o . -w . --steps main --profile thanos singularity --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37
nextflow -log ./thanos-10exomes_main/.main.nextflow.log run /home/tkoch/Sarek/main.nf -profile thanos,singularity --awsqueue none --sample /home/tkoch/sarek-10exomes/thanos-10exomes.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```

*germlineVC.nf* - 2019-03-19-9-10

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home/tkoch/sarek-10exomes/thanos-10exomes.tsv -o . -w . --steps germlineVC --profile thanos singularity --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37
nextflow -log ./thanos-10exomes_germlineVC/.germlineVC.nextflow.log run /home/tkoch/Sarek/germlineVC.nf -profile thanos,singularity --awsqueue none --tools HaplotypeCaller,strelka,mutect2 --sample ./thanos-10exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```

*annotate.nf* - 2019-03-20-9-18

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s /home/tkoch/sarek-10exomes/thanos-10exomes.tsv -o . -w . --steps annotate --profile thanos singularity --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37
nextflow -log ./thanos-10exomes_annotate/.annotate.nextflow.log run /home/tkoch/Sarek/annotate.nf -profile thanos,singularity --awsqueue none --tools snpeff --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```



#### 10 samples conda

*main.nf* - 2019-03-16-23-1

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-10exomes.tsv -o . -w . --steps main --profile thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37
nextflow -log ./thanos-10exomes_main/.main.nextflow.log run /home/tkoch/Sarek/main.nf -profile thanos,noContainers --awsqueue none --sample ./thanos-10exomes.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_main --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```

*germlineVC.nf* - 2019-03-17-9-22

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-10exomes.tsv -o . -w . --steps germlineVC --profile thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 -r
nextflow -log ./thanos-10exomes_germlineVC/.germlineVC.nextflow.log run /home/tkoch/Sarek/germlineVC.nf -profile thanos,noContainers --awsqueue none --tools HaplotypeCaller,strelka,mutect2 --sample ./thanos-10exomes/results/Preprocessing/Recalibrated/recalibrated.tsv --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_germlineVC --verbose -with-report -with-trace -with-timeline -with-dag -ansi -resume
```

*annotate.nf* - 2019-03-17-20-19

```bash
#!/usr/bin/env bash
# python /home/tkoch/nf-test-scripts/sarek-wrapper.py -aq_main none -aq_germ none -aq_an none -aq_mqc none -s ./thanos-10exomes.tsv -o . -w . --steps annotate --profile thanos noContainers --reports . --script_location /home/tkoch/Sarek --genome GRCh37 --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37
nextflow -log ./thanos-10exomes_annotate/.annotate.nextflow.log run /home/tkoch/Sarek/annotate.nf -profile thanos,noContainers --awsqueue none --tools snpeff --genome_base /home/tkoch/igenomes/Homo_sapiens/GATK/GRCh37 --genome GRCh37 --outDir ./thanos-10exomes/results -w ./thanos-10exomes/work "" --localReportDir ./thanos-10exomes_annotate --verbose -with-report -with-trace -with-timeline -with-dag -ansi
```