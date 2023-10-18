# Installation

# Install SDKMAN

*This is optional if you already have a working Java Development Kit (JDK) 
on your machine.*

Check your JDK installation:
```bash
java -version
```

[SDKMAN Installation Instructions](https://sdkman.io/install) (copied here)

```bash
curl -s "https://get.sdkman.io" | bash
```

Then it will load magic sdkman functions into your bash shell.

```bash
sdk list           # to see all possible jvm sdks you can instsall
sdk list java      # to see all possible JDKs you can install
sdk install java   # install the default JDK
sdk install kotlin # install latest kotlin
sdk install gradle # install latest gradle (build tool for jvm projects)
```
                   
You can show the above installed binaries on your path
```bash
echo $PATH
```

If you try to see SDKMAN on your path, you will see it is not there.


## Setup Kotlin IDEs

### IntelliJ IDEA
https://www.jetbrains.com/idea/download

Make sure to scroll down and download the Community Edition, which is free!
Otherwise you trial license of the Ultimate Edition will expire in a month.

Also make sure to choose the right binary for your CPU!

### Android Studio

[Download](https://developer.android.com/studio)
[System Requirements](https://developer.android.com/studio/install)

Also make sure to choose the right binary for your CPU!

### VSCode

[Setup the Kotlin plugin to VSCode](https://in-kotlin.com/ide/vscode/setup-vscode-for-kotlin-development/)
