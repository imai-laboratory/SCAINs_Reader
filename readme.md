# SCAIN Reader and analysis

## Intsallation
Install the packages via the following command: 
```shell
$ pipenv install
```

## Setup
### Download and extract dataset
Download and extract dataset via the following command: 
```shell
$ pipenv run setup
```

### Set OpenAI API key
Set your OpenAI API key as the environment variable: 
```shell
$ export OPENAI_API_KEY=<your OpenAI API key>
```

## Open Page
Open SCAINs_Reader's web page via the following command:
```shell
$ pipenv run main
```

## Analysis
Run `analysis_extraction.ipynb` and `analysis_survey.ipynb` to analyze the results.

### Latex package
Download udline.sty from [here](http://minamo.my.coocan.jp/tex/udline.html) to generate LaTeX source with underline.
