# fava-envelope

## memst/fava-envelope

[![Run on Repl.it](https://repl.it/badge/github/memst/fava-envelope)](https://repl.it/github/memst/fava-envelope)
_(clicking this replit link should let you create an actually working repl)_

This is a fork of [polarmutex/fava-envelope](https://github.com/polarmutex/fava-envelope) with a few changes, most notably:
- Removing pandas dependency (while making things faster)
- Caching envelope results until source files are changed
- Addition of multi-currency support
- Simplification existing budgeting table
- Chaged directive parsing to use ACCOUNT instead of STRING where appropriate
- New directives for better control of the extension's behaviour

Please check out the [changelog](https://github.com/memst/fava-envelope/blob/master/CHANGELOG.md) for a bit more details about what changed.

The syntax highlighting of this extension is supported in Sublime Text text editor by [my fork of norseghost/sublime-beancount](https://github.com/memst/sublime-beancount).

Please raise any issues if you confused about installation or usage. I'd be happy to help.

## Installation
Clone the repo and install it:
```bash
git clone https://github.com/memst/fava-envelope.git
python -m pip install -e fava-envelope
```

## Running fava-envelope

### Load the Extension
Add this to your beancount journal, and start fava as normal
```
2000-01-01 custom "fava-extension" "fava_envelope" "{}"
```

You should now see 'Envelope' in your fava window. You must set up a budget (see below), or else Fava will report a 404 error.

### Setting up budget

### Set the budget start date
start date in the format <4 digit year>-<2 digit month>
```
2020-01-01 custom "envelope" "start date" "2020-01"
```

### Budget months ahead
If you want to see future months (to budget ahead), set this parameter
```
2020-01-01 custom "envelope" "months ahead" "2"
```
The default is 0

### Set up Budget Accounts
You will need to specify the Assets and Liabilities you want included in your budget (For example ignoring Investment accounts). you can use regular expression in these statements
```
2020-01-01 custom "envelope" "budget account" "Assets:Checking"
2020-01-01 custom "envelope" "budget account" "Liabilities:Credit-Cards:*"
```

### Set up mappings
By default fava-envelope will use the Assets/Liabilities/Income/Expenses buckets that are not listed in the budget accounts. this directive allows you to map them to another bucket
```
2020-01-01 custom "envelope" "mapping" "Expenses:Food:*" "Expenses:Food"
```

### Allocate money to a bucket
```
2020-01-31 custom "envelope" "allocate" "Expenses:Food" 100.00
```

### Set up operating currency
The envelopes will read the operating currency from the core beancount option.
```
option "operating_currency" "EUR"
```
It will default to USD if this option is not set. Only a single currency is supported for the budget.
