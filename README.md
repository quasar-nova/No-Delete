# No Delete
> Suhas N | 2023

<h1> This program is distributed under the MIT License and is for educational purposes ONLY. The authors / contributors of this program
are not responsible for ANY DAMAGES CAUSED to YOU or YOUR ORGANIZATION. </h1>

## Description
This program injects into `explorer.exe` and plays with its Shift+Delete functionality.
The file which is `Shift+Delete`-ed will be hidden for a while and moved to the `store/{unix-epoch}` directory.
You will know where to use this program.

Read about the inner workings [here](https://sp1d3r.vercel.app/posts/explorer-nodelete/)

## Usage
I recommend you to create a seperate directory.
1. Grab `NoDelete.exe` and `NoDeleteH.dll` files from `Releases` and place them in the same folder.
2. Start `NoDelete.exe` program. It will download `shell32.pdb` (10-11MB, speed depends on MS symbol servers)
3. If the program ends, check the logs in the `log` folder.
4. The logs in the log folder as named as follows:
	+ `base.log`: contains information of the main executable
	+ `inject_{PID}.log`: contains information of the target process.

**For every windows update (not product/.NET updates), you should delete the `shell32.pdb` file and regenerate it.**

## Heads up
Yet to implement the `auto-injection` feature. This will be implemented on demand.

## Disclaimer
I am not responsible for any damage caused to you by using this source code.
Don't be scared if `explorer.exe` crashes but report the issue in #Issues with your logs.
