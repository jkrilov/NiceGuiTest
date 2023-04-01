# TerraformAzureActionTemplate

This repo will have some basic folder structure and a GitHub action for deploying Terraform IaC to Azure.  It will serve as a template for future projects/lab work. 

## Azure Integration

In order for Terraform to be able to connect to Azure you'll need to [create a service principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) along with a secret. Once you create the service principal add the following secrets to your Github Repo under **Repo Settings > Secrets and variables > Actions**:

* AZURE_CLIENT_ID
* AZURE_CLIENT_SECRET
* AZURE_SUBSCRIPTION_ID
* AZURE_TENANT_ID

## Github Actions

There are several workflows in this template which can be found under _[./.github/workflows](./.github/workflows)_.  Keep in mind these are very simple examples meant for my lab, and would not be appropriate for most production deployments. 

### Terraform-destroy.yml

This workflow installs Terraform and then runs `terraform destory`. This is helpful for cleaning up lab environemnts so you don't get billed for something you're not using. 

### Terraform-docs.yml

This workflow used a pre-built action to run [Terraform Docs](https://github.com/terraform-docs/gh-actions). There is a config file located in the _./terraform_ directory which allows for customization.  This action also supports more advanced configurations such as nested modules and Atlantis files. This workflow runs on any pull request and ensures that documentation markdown is generated before merging the pull request. 

### Terraform-plan-apply.yml

This is the core worklfow which actually applies the IaC (Infrastructure as Code) using Terraform. This workflow performs a number of actions:

1) **TFLint** - This step runs a pre-built github action that runs TFLint and leaves appropriate comments directly on the code in the pull-request. [reviewdog/action-tflint@master](https://github.com/reviewdog/action-tflint)
1) **Terraform Format**
1) **Terraform Validate**
1) **Terraform Init**
1) **Terraform Plan**
1) **PR Comment Script** - This step runs a custom bash script based on a script [provided by Hashicorp](https://developer.hashicorp.com/terraform/tutorials/automation/github-actions).  The script takes the output from the previous steps including the full Terraform Plan output and submits them as a comment on the PR for easy review.
1) **Terraform Apply** - Once the PR has been merged into the main branch (or upon any commit directly to the main branch) the final action is to run Terraform Apply. This step will only run if the Terraform Apply step was successful. 

## Terraform Docs

The output from Terrform Docs can be found: [here](/terraform/README.md)

## References

1) [GitHub Actions](https://docs.github.com/en/actions)
1) [Terraform](https://developer.hashicorp.com/terraform/intro)
1) [Terraform Docs](https://terraform-docs.io/user-guide/introduction/)
1) [Terraform Linter](https://github.com/terraform-linters/tflint)
1) [Markdown](https://www.markdownguide.org/getting-started)
