set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable 
set showcmd
set ruler 
set encoding=utf-8
set showmatch
"set sw=2
set relativenumber
set laststatus=2
set noshowmode

call plug#begin('~/.local/share/nvim/plugged')

" Themes
Plug 'tomasiser/vim-code-dark'

" IDE
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'airblade/vim-gitgutter'
Plug 'scrooloose/nerdcommenter'
Plug 'christoomey/vim-tmux-navigator'
Plug 'Yggdroot/indentLine'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'dense-analysis/ale'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'mkitt/tabline.vim'
Plug 'bling/vim-bufferline'
"Plug 'zefei/vim-wintabs'
"Plug 'Xuyuanp/nerdtree-git-plugin'
"Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
"Plug 'ryanoasis/vim-devicons'

"Go specific support
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

call plug#end()

colorscheme codedark
let g:airline_theme='minimalist'
let g:airline#extension#tabline#enabled = 1
let g:airline#extension#tabline#fnamemod = ':t'
"let g:airline_powerline_fonts = 1

let g:indentLine_fileTypeExclude = [ 'text', 'sh', 'help', 'terminal' ]
let g:indentLine_bufNameExclude = [ 'NERD_tree.*', 'term:*' ]

let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
let g:ale_set_loclist = 0
let g:ale_set_quickfix = 0 

let mapleader=" " 
nmap <Leader>s <Plug>(easymotion-s2) 
nmap <Leader>nt :NERDTreeFind<CR> 
let NERDTreeQuitOnOpen=1 
nmap <Leader>/ <Plug>NERDCommenterToggle
vmap <Leader>/ <Plug>NERDCommenterToggle
let g:NERDTreeGitStatusWithFlags = 1
let g:NERDTreeIgnore = ['^node_modules$' ]
command! -nargs=0 Prettier :CocCommand prettier.formatFile
nmap <Leader>j <Plug>(ale_previous_wrap)
nmap <Leader>k <Plug>(ale_next_wrap)


nmap <Leader>w :w<CR>
nmap <Leader>q :q<CR>
nmap <Leader>bd :bd<CR>
nmap <Leader>wq :wq<CR>
nmap ' $
vmap ' $
map <C-s> :w<CR>
nmap <C-l> :noh<CR>
vmap <C-l> :noh<CR>
nmap 5 %
vmap 5 %
"File management 
"Interesting commands: 
" 	:cd
" 	:lcd
" 	:newtab
" 	:e
" 	gt
nmap <Leader>fz :Files<CR> 
"  Go to tab by number
map <C-w> gt
map <C-q> gT
nmap <Leader>vim :tabnew /home/anyel/.config/nvim/init.vim<CR>
noremap <leader>1 1gt
noremap <leader>2 2gt
noremap <leader>3 3gt
noremap <leader>4 4gt
noremap <leader>5 5gt
noremap <leader>6 6gt
noremap <leader>7 7gt
noremap <leader>8 8gt
noremap <leader>9 9gt
noremap <leader>0 :tablast<cr>

" Go to buffer by number
noremap <leader>b1 :1b<CR>
noremap <leader>b2 :2b<CR>
noremap <leader>b3 :3b<CR>
noremap <leader>b4 :4b<CR>
noremap <leader>b5 :5b<CR>
noremap <leader>b6 :6b<CR>
noremap <leader>b7 :7b<CR>
noremap <leader>b8 :8b<CR>
noremap <leader>b9 :9b<CR>
noremap <leader>bb :bnext<CR>


"====================================================================================================================
"=============================================COC-Extensions=========================================================
"====================================================================================================================
let g:coc_global_extensions = [
  \ 'coc-pairs',
  \ 'coc-eslint', 
  \ 'coc-prettier', 
  \ 'coc-json', 
  \ ]


" from readme
" if hidden is not set, TextEdit might fail.
set hidden " Some servers have issues with backup files, see #649 set nobackup set nowritebackup " Better display for messages set cmdheight=2 " You will have bad experience for diagnostic messages when it's default 4000.
set updatetime=300

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight symbol under cursor on CursorHold
autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <F2> <Plug>(coc-rename)

" Remap for format selected region
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Create mappings for function text object, requires document symbols feature of languageserver.
xmap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap if <Plug>(coc-funcobj-i)
omap af <Plug>(coc-funcobj-a)

