while true
do
   heroku logs | grep -E 'account-activation|reset-password|task-feed|unsubscribe|project-review|task|Daemo Team|rejected'  >> heroku.log 2>&1
done
