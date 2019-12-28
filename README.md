# windows-terminal-base16-term

Convert base16-shell to Windows Terminal schemes.

## Windows Terminal in Cupcake

Applied scheme to WSL.

![cupcake](https://raw.githubusercontent.com/moeKiwiSAMA/windows-terminal-base16-term/master/img/screenshot.png)

## How to add scheme to Windows Terminal

First, open Windows Terminal Settings file.
You can press `Ctrl + ,` or find it at the top of the terminal.

Then, you will find lines like these:

```json
// .......
        "source": "Windows.Terminal.Wsl"
    }
],

// Add custom color schemes to this array
"schemes": [],

// Add any ....
// ........
```

Replace `"schemes":[]`with content in schemes.json, you can find it in [releases](https://github.com/moeKiwiSAMA/windows-terminal-base16-term/releases).
Don't forget with the `,(comma)`.

Add the scheme you choosed to terminal profile:

```json
{
  "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
  "hidden": false,
  "name": "Ubuntu-18.04",
  "colorScheme" : "base16-cupcake",// Here.
  "cursorColor": "#ab9bab",
  "fontFace": "DejaVuSansMono NF",
  "source": "Windows.Terminal.Wsl"
}
```

ColorScheme is the name of the scheme.  
Because of the limitation of the Windows Terminal, you may need to add cursorColor manually.  
The white color in the scheme is recommended.

You can get more information [here](https://github.com/microsoft/terminal/blob/master/doc/user-docs/UsingJsonSettings.md).

For a better experience, I suggest you to install [Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts) with Windows Compatible.

## Generate schemes json by yourself

```bash
git clone https://github.com/moeKiwiSAMA/windows-terminal-base16-term.git
cd windows-terminal-base16-term
python3 generate.py
```
