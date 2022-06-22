#!/usr/bin/env ruby
match = ARGV[0].scan(/(?<=from:)([^\]]*)/)
match.append(ARGV[0].scan(/(?<=to:)([^\]]*)/))
match.append(ARGV[0].scan(/(?<=flags:)([^\]]*)/))

puts match.join(',')
