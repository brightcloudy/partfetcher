curl -G https://octopart.com/api/v3/parts/match -d queries="[{\"mpn\":\"$1*\"}]" -d apikey="$2" -d exact_only=false -d pretty_print=true -d include[]=descriptions | grep value | head -n 1 > value
