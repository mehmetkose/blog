---
author: "Mehmet Köse"
date: 2019-04-03
title: Macos'ta Fish Shell Kurulumu
featuredImg: ""
tags: 
  - fish
  - shell
  - macos
---

Macos'ta zsh zamanın behrinde default olmuş, bilgisayarım son birkaç mojor versiyonu alamamıştı. İş yeri bilgisayarında 16" Macbook PRO'ya geçmiş bulunduk. ZSH'den Fish'e geçiyorum. Bash değiştirmesi her zaman sıkıntılı bir konu. 

Öncelikle bilgisayardaki shelllerimize bir bakalım

ls -l /bin/*sh

Fish'i kuralım

brew install fish

yoksa ekleyelim 

sudo bash -c 'echo /usr/local/bin/fish >> /etc/shells'

sonra fish'i default shell yapalım

chsh -s /usr/local/bin/fish


Bu noktada fish'i kurmuş olduk. Oh-my-zsh'i de kurarak devam ediyoruz.

curl -L https://get.oh-my.fish | fish

temayı değiştirelim
omf install bira


brew binary'lerini fish path'e ekleyelim

set -U fish_user_paths /usr/local/bin $fish_user_paths

mkdir -p ~/.config/fish

~/.config/fish/config.fish içine 

set -x LANG en_US.UTF-8
set -g -x PATH /usr/local/bin $PATH

ekleyelim.



The Fuck kurulumu


brew install jq &&
brew install grc &&
brew install thefuck &&
omf install spark &&
omf install license &&
omf install battery &&
omf install git-flow &&
omf install await &&
omf install hash &&
omf install errno &&
omf install brew &&
omf install node-binpath &&
omf install grc &&
omf install pj &&
set -gx PROJECT_PATHS ~/Library/Projects &&
omf install thefuck




https://gist.github.com/ghaiklor/5c393e1c27cab79a9258

https://gist.github.com/gagarine/cf3f65f9be6aa0e105b184376f765262

https://medium.com/tuannguyendotme/set-up-the-fish-shell-on-mac-step-by-step-6a77bcb2687c

https://reckoning.dev/fish-shell

https://reckoning.dev/fish-shell

https://medium.com/almoullim/from-bash-to-zsh-to-fish-e432f1e1b9f8