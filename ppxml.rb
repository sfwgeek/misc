#!/usr/bin/env ruby
# vim: et sw=2 ts=2:

#--
# Command Line Program (CLI) to pretty print XML.
# File paths are supplied as program arguments.  Each file is parsed and outputted to standard output.
#++
#


# Dependencies.
require 'rexml/document'


def prettyPrintXmlFile(srcFilePath, output=$stdout)
  if File.file?(srcFilePath)
    xmlStr = File.open(srcFilePath, 'rb').read
    xmlDoc = REXML::Document.new(xmlStr)
    xmlFormatter = REXML::Formatters::Pretty.new
    xmlFormatter.compact = true # Have open and close tags on same line.
    xmlFormatter.write(xmlDoc, output)
  else
    puts('File does not exist: ' + srcFilePath)
  end
end

def main()
  ARGV.each do|arg|
    prettyPrintXmlFile(arg)
  end 
end


# Program entry point.
if __FILE__ == $0
  main()
end
