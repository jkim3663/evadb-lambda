### Implementation Details
The initial proposal was connecting EvaDB via AWS Lambda. However, due to technical
difficulties that are related to Lambda and EvaDB installation packages (discussed more in the
Challenges section), I decided to set up the EvaDB environment on a AWS EC2 instance and
bootstrap it with other AWS services such as Lambda, S3, etc. Currently the Python script inside
the EC2 instance is able to run EvaDB queries, store the output, and upload it to a S3 storage
bucket. This functionality has the potential to be extended. Appendix A includes the steps and
Linux commands for the environment set up. Appendix B includes the code snippet that runs
basic query from the EC2 instance, and transfers the query output to AWS S3 (object storage)
using boto3 package.

### Metrics
The current AWS EC2 instance only contains the minimum requirements to run EvaDB, so it
does not have heavy packages and additional dependencies such as PostgreSQL or MySQL
related packages. With the given constraint, the cost for running EvaDB from an EC2 instance
does not create any unnecessary costs, and remaining in the AWS free-tier proves it. However,
even the compressed minimum packages go over 50Mb, which means that when later adding the
packages to Lambda or other services directly, it is important to reduce the size and carefully
choose additional packages depending on the implementation. If not, EvaDB might not compile
or create unnecessary costs.

### Lessons Learned
I learned how pip package installation works and how EvaDB’s package is set up. I had to
thoroughly analyze the requirements from both AWS instances and EvaDB in order to run the
queries. There were multiple factors to consider such as the operating system, the size / memory
of the instance, particular constraints such as Lambda’s layer size. Moreover, I had to ensure that
the packages are as small as possible, and it is cost-free (at least for this scope) so that running
EvaDB from the cloud is compelling and achievable. If simply running EvaDB required a lot of
space and money, then it would rather be optimal to run locally.

### Implementation Challenges
I changed the objective of this project from initially running EvaDB from AWS Lambda to
running EvaDB from AWS EC2 instance, and later planning to extend its functionalities to other
AWS services. The reason is that to run EvaDB from Lambda, it was required to install EvaDB
and its dependent packages such as NumPy, Pandas, etc. There were multiple approaches I
attempted to enable this feature but failed. First, I tried installing packages directly from local,
zip the packages, upload it to AWS S3, and add it as a layer to Lambda. This did not work
because Lambda runs on AWS Linux 2, which is a different operating system. The next approach
was using AWS Cloudshell. However, Cloudshell provides only a small amount of storage and
makes it difficult to install all the packages needed before compressing them. Then, I created an
EC2 instance through AWS Cloud9 IDE. A naive installation of the packages made the zip file
size excessive as 2.1 Gb, while Lambda only accepts up to 60 Mb, so I had to install all of the
packages one-by-one with no dependencies to reduce the size. While this finally made Lambda
recognize the packages, EvaDB by its basic configuration, writes files such as “evadb.yml” or
creates directories like “evadb_data.” Lambda only accepts file writes on the “/tmp” directory. I
was able to change “evadb_data” directory to inside the “tmp” directory, but to change the
location of “evadb.yml,” I had to go through changing multiple files without breaking all the
dependencies. I concluded this would require much more time and effort; hence, I altered the
objective of the project to instantiate EvaDB from EC2 instance, and then further bootstrap it
with other services potentially.

