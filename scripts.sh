AOC="$HOME/Documents/advent-of-code"
AOC_COOKIE=$(cat "$AOC/.session" 2>/dev/null)

function aoc-load () {
  if [ $1 ]
  then
    curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > "day$(printf "%02d" $2)_input.txt"
  else
    current_day=$(date +%d)
    url_day=$(echo $current_day | sed 's/^0//')
    
    curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day`)/$url_day/input" > "day${current_day}_input.txt"
  fi
}