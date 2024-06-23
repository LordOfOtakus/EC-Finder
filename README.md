# EC-Finder
Python script to help find Pokemon that will have an Encryption Constant divisible by 100, when used with Pokefinder

><p>For those unaware, the way Dudunsparce chooses to evolve into Two or Three Segment form is based on the Pokemon's Encryption Constant. If the EC is divisible cleanly by 100, it'll be a Three-Segment, Two-Segment otherwise.
>Tools like PokeFinder will tell you the Encryption Constant for whatever mon you're trying to RNG, but its displayed in the original Hexadecimal, and there's no way to filter for something like "divisible by 100."
>You can, however, export all of the "hits" in PokeFinder as a text file. Once you have your RNG set up and information popped into PokeFinder, export the hits as a text file, then run the attached python script in terminal or the command line with the file as an argument. (If you've used BDSP Rng before, you should know how.) It should print the Advances in Terminal that have a Pokemon whose Encryption Constant is divisible by 100.
>Example for the script on Mac:
>
>>python EC\ Finder.py (filename).txt
>
>If you aren't running the command line in the directory where the files are located, dragging them to the terminal to autofill their locations also works.
>
>>python /Users/[REDACTED]/Desktop/BDSP\ RNG/EC\ Finder.py /Users\[REDACTED]\Desktop/BDSP\ RNG/(filename).txt</p>
