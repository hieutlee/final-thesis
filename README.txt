
==============================================================================
 FlickrLogos-32
 http://www.multimedia-computing.de/flickrlogos/
==============================================================================
    
The dataset FlickrLogos-32 contains photos depicting logos and is meant for 
the evaluation of multi-class logo detection in real-world images. 
We collected logos of 32 different logo classes by downloading them from Flickr. 
All logos have an approximately planar surface.  The specific classes were 
determined by trial-and-error and mostly chosen by the number of logos 
we could quickly retrieve by querying the Web service with appropriate queries. 

==============================================================================
 Classes
==============================================================================
There are 32 logo classes: Adidas, Aldi, Apple, Becks, BMW, Carlsberg, 
Chimay, Coca-Cola, Corona, DHL, Erdinger, Esso, Fedex, Ferrari, Ford, Fosters, 
Google, Guiness, Heineken, HP, Milka, Nvidia, Paulaner, Pepsi, Ritter Sport, 
Shell, Singha, Starbucks, Stella Artois, Texaco, Tsingtao and UPS.

See http://www.multimedia-computing.de/flickrlogos/ for more details

==============================================================================
 Authors
==============================================================================
Stefan Romberg, stefan.romberg@informatik.uni-augsburg.de

If you use this dataset in your work please cite the following paper:

Scalable Logo Recognition in Real-World Images
Stefan Romberg, Lluis Garcia Pueyo, Rainer Lienhart, Roelof van Zwol
ACM International Conference on Multimedia Retrieval 2011 (ICMR11), Trento, April 2011. 

==============================================================================
 Tools
==============================================================================
 There is a helper script in <basedir>/scripts/copy_images_to_flat_dir.py
 that copies the files in the nested directories <basedir>/classes/*
 to "flat" directories in <basedir>/flat/*.
 
==============================================================================
 Changelog
==============================================================================
16 May 2012:
- Added binary masks for images that contain a logos:
  Each logo image in <basedir>/classes/<class>/<file>.jpg has its mask 
  in <basedir>/masks/<class>/<file>.mask.<n>.png where n is the mask number starting at 0.
  
- Added merged masks:
  Each logo image in <basedir>/classes/<class>/<file>.jpg has its merged mask 
  in <basedir>/masks/<class>/<file>.mask.merged.png
  
- Masks are single-channel PNG images of the same size as the original image. 
  Masked areas have the value 255, unmasked areas 0.

08 Feb 2012:
- Added thumbnails.
- Added more .txt files holding filenames in various formats:
  *.filenames.txt holds plain file name without paths including file extenson
  *.fullpaths.txt holds the full path of every file
  *.relpaths.txt hold the path of every file relative to the base directory of this dataset.
  *.spaces.txt holds files and class names separated by spaces.