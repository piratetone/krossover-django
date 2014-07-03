from django.db import models

class Coach(models.Model):
  email_address = models.CharField(max_length = 200)
  school_name = models.CharField(max_length = 200)
  sport = models.CharField(max_length = 50)
  kredit = models.CharField(max_length = 5, default = 0)


  BASKETBALL = 'Basketball'
  FOOTBALL = 'Football'
  VOLLEYBALL = 'Volleyball'
  LACROSSE = 'Lacrosse'

  sport_choices = (
    (BASKETBALL, 'Basketball'),
    (FOOTBALL, 'Football'),
    (LACROSSE, 'Lacrosse'),
    (VOLLEYBALL,'Volleyball')
  )
  sport = models.CharField(max_length=10, choices=sport_choices)

  def __unicode__(self):
   return self.school_name +' ' + self.sport
  

  def award_kredit(kredit_earned):
   self.kredit += int(kredit_earned)
