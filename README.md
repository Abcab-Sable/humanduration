# **A good "human-friendly duration" library should let people:**
1. Parse natural duration strings (flexible, forgiving)
2. Convert them into proper `timedelta` objects
3. Format durations back into readable strings
4. Do basic combination/comparison operations
5. Validate or reject malformed input
6. Provide a clean Python API - easy to remember, easy to use

# Input Parsing - the core feature
You want to support strings humans naturally write, such as:
**Compact formats**
```python
"1h"
"30m"
"90s"
"10d"
```
**With spaces**
```python
"1 h"
"1 h 30 m"
```
**Combined formats**
```python
"1h 30m"
"2d 4h"
"3h 20m 10s"
"2 days, 3 hours and 5 seconds"
```
**Plurals and long unit names**
```python
"day", "days"
"hr", "hour", "hours"
"min", "mins", "minute", "minutes"
```
**Decimal values**
```python
"1.5h" -> 1 hour 30 minutes
"2.25 days"
"0.5h" -> 30 minutes
```
**Negative durations**
```python
"-5m"
```
**Invalid input throws a clean exception**
```python
parse_duration("1x") -> DurationParseError
```
