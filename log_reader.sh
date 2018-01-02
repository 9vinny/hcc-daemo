while true
do
   heroku logs | grep account-activation  >> heroku.log 2>&1
done
