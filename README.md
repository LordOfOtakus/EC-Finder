# PokeFinderHelper
Python script to help find certain Pokemon lacking filter options in PokeFinder

<p> This program is designed to assist in finding 3 things, Three-Segment Dudunsparce, Wurmple evolutions, and Jumbo / Teeny Pokemon. PokeFinder gives you the information necessary to find these, but its rather slow by hand. Since PokeFinder lets you export all the "hits" it finds, you can take the exported text file and have this program read through it, and find what you're looking for.
  
For those unaware, the way Dudunsparce and Wurmple decide their evolutions is based on their Encryption Constant. PokeFinder tells you the Encryption Constant for every advance, but you can't filter for certain ones.
Similarly. It tells you the Height of wild Pokemon (and perhaps eggs later), but you can't filter for 255 or 0 Height.

Once you have your RNG set up and information popped into PokeFinder, export the hits as a text file, then run the attached python script in terminal or the command line and follow the instructions. (If you've used BDSP Rng before, you should know how.) It should print the Advances in Terminal that have a Pokemon whose Encryption Constant is divisible by 100.



# Frequently Asked Questions

<p>To be added...</p>
