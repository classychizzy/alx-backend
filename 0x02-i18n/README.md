# alx-backend
0x02. i18n

### Extract your message ids using

`pybabel extract -F babel.cfg -o messages.pot .`


### build your dictionaries using

`pybabel init -i messages.pot -d translations -l en`
`pybabel init -i messages.pot -d translations -l fr`

where en or fr can be replaced with any country code


### or update your dictionaries using

`pybabel update -i messages.pot -d translations -l en`
`pybabel update -i messages.pot -d translations -l fr`

### Then compile the translations using

`pybabel compile -d translations`

