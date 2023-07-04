#!/usr/bin/env ruby
#The regular expression must match School
#The Script uses a string literal to match the input
#string
puts ARGV[0].scan(/School/).join
