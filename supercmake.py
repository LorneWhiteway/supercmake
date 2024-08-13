#!/usr/bin/env python

    
def supercmake_filename():
    return "super_cmake.cmake"
    
    
        
def supercmake(top_directory):
    import fnmatch
    import os
    
    anything_found = False
    
    abs_top_directory = os.path.abspath(top_directory)
    
    output_filename = os.path.join(abs_top_directory, supercmake_filename())

    with open(output_filename, 'w') as outfile:
        for root, dirnames, filenames in os.walk(abs_top_directory):
            for filename in (fnmatch.filter(filenames, 'CMakeLists.txt') + fnmatch.filter(filenames, 'Find*.cmake')):
                anything_found = True
                full_file_name = os.path.join(root, filename)
                print(full_file_name)
                outfile.write("\n")
                outfile.write("#---------------------------------------------------------------------------------------------------" + "\n")
                outfile.write(full_file_name + "\n")
                outfile.write("#---------------------------------------------------------------------------------------------------" + "\n")
                outfile.write("\n")
                with open(full_file_name) as infile:
                    outfile.write(infile.read())
                    
    if not anything_found:
        print("No cmake files found")
    else:
        print("Output written to {}".format(output_filename))
        
    
    
if __name__ == '__main__':

    import sys
    if len(sys.argv) != 2:
        print("Usage: {} <startdirectory>".format(__file__))
        print("Creates file {} in <start directory>.".format(supercmake_filename()))
    else:
        supercmake(sys.argv[1])
  
    
    
    
