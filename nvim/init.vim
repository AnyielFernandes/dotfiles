set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable 
set showcmd
set ruler 
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2
set noshowmode

call plug#begin('~/.local/share/nvim/plugged')

" Themes
Plug 'tomasiser/vim-code-dark'

" IDE
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

colorscheme codedark
let g:airline_theme='minimalist'
let g:airline#extension#tabline#enabled = 1
let g:airline#extension#tabline#fnamemod = ':t'
"let g:airline_powerline_fonts = 1



let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
let NERDTreeQuitOnOpen=1

nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
