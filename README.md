Some Screenshots: 

1. get all the free slots and booked slots. 

![Screenshot from 2024-06-24 17-15-37](https://github.com/wolf3766/oneassure/assets/76847651/ba89dced-1150-473b-9596-cddc882d98ed)


![Screenshot from 2024-06-24 17-15-41](https://github.com/wolf3766/oneassure/assets/76847651/885537ab-23e2-4d0b-a122-dcc58e1c0e1b)


![Screenshot from 2024-06-24 17-16-20](https://github.com/wolf3766/oneassure/assets/76847651/a7603443-a55f-4188-b144-ef0a0e6d63f5)


![Screenshot from 2024-06-24 17-17-34](https://github.com/wolf3766/oneassure/assets/76847651/c88b0c30-bbed-4e0a-be89-795450530a16)


![Screenshot from 2024-06-24 17-17-46](https://github.com/wolf3766/oneassure/assets/76847651/bd2fa8bc-f1a3-4ceb-a3e5-e23ea595750b)


language: python. 
framework: django. 
database: sqlite
notifcation is implemented using celery and redis db. 

API's: 
 Create a new user.
2. Update the user’s `dnd_start_time`  , `dnd_end_time` ,`preferred_timezone`
3. Create new meetings for that particular user
4. Given a *start_time* and an *end_time ,* return the booked meetings, as well as the free time slots.
5. Notify the user about their meetings based on the `notification_interval` cron. The notification should be sent based on the user’s `preferred_timezone`  and should NOT be sent between `dnd_start_time`  and `dnd_end_time`

