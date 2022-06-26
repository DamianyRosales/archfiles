set exrc
set guicursor=
set relativenumber
set nohlsearch
set hidden
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set termguicolors
set scrolloff=8
set completeopt=menuone,noinsert,noselect
set colorcolumn=80
set signcolumn=yes

set encoding=UTF-8

syntax on

" plugins

call plug#begin('~/.vim/plugged')
    Plug 'nvim-telescope/telescope.nvim'
    " Theme
    Plug 'sainnhe/everforest'
    Plug 'mhartington/oceanic-next'
    Plug 'gruvbox-community/gruvbox'
    Plug 'nekonako/xresources-nvim'
    Plug 'marko-cerovac/material.nvim'    
    Plug 'elianiva/gruvy.nvim'
    " Syntax
    Plug 'sheerun/vim-polyglot'
    " File explorer tab
    Plug 'scrooloose/NERDTree'
    " Dev icons in file explorer
    Plug 'ryanoasis/vim-devicons'
    " Auto pair ()[]{}
    Plug 'jiangmiao/auto-pairs'
    " Autocompletion
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    " Better syntax highlighting
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}   
    " Vim airline and airline themes
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
call plug#end()

source $HOME/.config/nvim/plug-config/coc.vim
source $HOME/.config/nvim/highlight.lua

" colorscheme

colorscheme everforest
" colorscheme OceanicNext
" colorscheme gruvbox
" colorscheme gruvy

" Material -->
"    colorscheme material
"    let g:material_style = "deep ocean"

highlight Normal guibg=none
highlight NonText ctermbg=none
highlight EndOfBuffer guibg=NONE ctermbg=NONE

" enables
" --> Airline
    let g:airline#extensions#tabline#enabled = 1
    let g:airline#extensions#tabline#formatter = 'jsformatter'
    let g:airline_powerline_fonts = 1
    "let g:airline_theme='solarized'
    "let g:airline_solarized_bg='dark'

"remaps

" --> NERDTree

    nnoremap <C-n> :NERDTree<CR>
    nnoremap <C-t> :NERDTreeToggle<CR>
    nnoremap <C-f> :NERDTreeFind<CR>

    autocmd VimEnter * NERDTree
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Go to next tab and previous tab
    
    nnoremap <C-e> :bnext<CR>
    nnoremap <C-q> :q!<CR>

" Save file
    nnoremap <C-s> :w<CR>
" Quit
    nnoremap <C-z> :tabnew<CR>
