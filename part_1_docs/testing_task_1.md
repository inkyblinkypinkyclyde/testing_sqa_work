### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:                    # You can't assign a value to a variable in an if statement. This needs an extra =
      return True
    else                                  # There should be a semi colon after else
      return False
   

  dif highest_card(self, card1 card2):    # card1 and card2 are not comma seperated, def is also spelled incorrectly
  if card1.value > card2.value:           # this and the following three lines are missing one indentation level
    return card                           # card is not defined
  else:
    return card2
  


def cards_total(self, cards):             # this isn't indented either. This would not be included in the CardGame class but is instead floating around on it's own
  total                                   # python doesn't let you declare a variable without giving it a value
  for card in cards:                      
    total += card.value
    return "You have a total of" + total  # this indent is part of the for loop so the loop will only run once. You also can't add an int to a str.
  
```
