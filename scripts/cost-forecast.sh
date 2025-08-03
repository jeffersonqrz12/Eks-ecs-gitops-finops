aws ce get-cost-forecast \
  --time-period Start=$(date +%F),End=$(date -d "+7 days" +%F) \
  --metric BLENDED_COST \
  --granularity DAILY \
  --region us-east-1 \
  --profile default
