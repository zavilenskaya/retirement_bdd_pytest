Feature: calculate_retirement_age
    As a visitor of www.ssa.gov web site, I want to use the retirement calculator to calculate the full age and month of retirement depending on year of birth.

    Scenario: Testing with 1959 birth year
        Given calculate retirement age function
        When the year of birth  "1959" is entered
        Then results for age of retirement is '(66, 10)'

    Scenario: Testing with 1800 birth year
        Given calculate retirement age function
        When the year of birth  "1800" is entered
        Then results for age of retirement is 'Birth year "1800" must be no earlier than 1900'

    Scenario: Testing with 3001 birth year
        Given calculate retirement age function
        When the year of birth  "3001" is entered
        Then results for age of retirement is 'Birth year "3001" must be earlier than 3000'

    Scenario: Testing with 3000 birth year
        Given calculate retirement age function
        When the year of birth  "3000" is entered
        Then results for age of retirement is 'Birth year "3000" must be earlier than 3000'



    Scenario Outline: Testing with valid data age
        Given calculate retirement age function
        When the year of birth "<birth_year>" is entered
        Then results for age of retirement "<age_years>", "<age_month>" with "<birth_year>"

       Examples:
          | birth_year   | age_years | age_month |
          | 1937         | 65        |0          |
          | 1938         | 65        |2          |
          | 1939         | 65        |4          |
          | 1940         | 65        |6          |
          | 1941         | 65        |8          |
          | 1942         | 65        |10         |
          | 1943         | 66        |0          |
          | 1947         | 66        |0          |
          | 1954         | 66        |0          |
          | 1955         | 66        |2          |
          | 1956         | 66        |4          |
          | 1957         | 66        |6          |
          | 1958         | 66        |8          |
          | 1959         | 66        |10         |
          | 1960         | 67        |0          |
          | 1965         | 67        |0          |


#Feature: calculate_retirement_date
 # As a visitor of www.ssa.gov web site, I want to use the retirement calculator to calculate the date and month of retirement depending on year and month of birth

    Scenario Outline: Testing with valid data retirement_date
        Given calculate_retirement_date function
        When the year of birth "<birth_year>", month of birth "<birth_month>", age of retirement "<age_years>", month of retirement  "<age_month>" is entered
        Then results for year "<ret_year>" and month of retirement "<ret_month>"is returned, with "<birth_year>", "<birth_month>", "<age_years>", "<age_month>"
        Examples:
      | birth_year | birth_month | age_years|age_month|ret_year| ret_month|
      | 1981       |11           |67        | 0       | 2048   | 11       |
      | 1935       |8            |65        | 0       | 2000   | 8        |
      | 1900       |11           |65        | 0       | 1965   | 11       |
      | 2999       |11           |65        |0        | 3064   | 11       |
      | 1970       |1            |67        |0        | 2037   | 1        |
      | 1970       |12           |65        |0        | 2035   | 12       |
      | 1959       |12           |66        |11       | 2026   | 11       |



    Scenario Outline: Testing with invalid data retirement_date
        Given calculate_retirement_date function
        When the year of birth "<birth_year>", month of birth "<birth_month>", age of retirement "<age_years>", month of retirement  "<age_month>" is entered
        Then appropriate error message is returned "<error_message>" with "<birth_year>", "<birth_month>", "<age_years>", "<age_month>"
        Examples:
      | birth_year |  birth_month | age_years | age_month | error_message |
      | 1800       | 9            | 65        | 0         | 'Birth year "1800" must be no earlier than 1900'|
      | 3005       | 9            | 65        | 0         | 'Birth year "3005" must be earlier than 3000'   |
      | 1965       | 18           | 65        | 0         | 'Birth month "18" must be between 1 and 12'     |
      | 1965       | 0            | 65        | 0         | 'Birth month "0" must be between 1 and 12'      |
      | 1965       | 9            | 55        | 0         | 'Age year "55" must be between 65 and 67'       |
      | 1965       | 9            | 70        | 0         | 'Age year "70" must be between 65 and 67'       |
      | 1965       | 9            | 67        |-1         | 'Age month "-1" must be between 0 and 11'       |
      | 1965       | 9            |67         | 12        | 'Age month "12" must be between 0 and 11'       |