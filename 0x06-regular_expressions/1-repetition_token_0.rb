#!/usr/bin/env ruby
#The regular expression will match a
#specified set of cases
puts ARGV[0].scan(/hbt{2,5}n/).join
