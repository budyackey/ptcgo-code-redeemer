# ptcgo-code-redeemer
Automated Pokemon TCG pack code redemption tool.

### Requirements
* Install the required Python packages: `python3 -m pip install selenium colorama`.
* Install [geckodriver](https://github.com/mozilla/geckodriver/releases/latest) and make sure it is in your `PATH`.
* The script requires that the user provides a text file containing PTCGO codes, one per line.
* When the script starts, the user is logged in.  the script then pauses until the user completes the captcha.

### Usage
`python3 pokemon_redeemer.py <codes file>`
