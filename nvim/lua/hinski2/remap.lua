vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

-- Indent / unindent w VISUAL mode
vim.keymap.set("v", ">", ">gv", { noremap = true, silent = true })
vim.keymap.set("v", "<", "<gv", { noremap = true, silent = true })

-- Ctrl+Backspace 
vim.keymap.set("i", "<C-BS>", "<C-w>", { noremap = true })
vim.keymap.set("i", "<C-H>", "<C-w>", { noremap = true })

-- show error under the cursor
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { noremap = true, silent = true })

-- make comment
vim.keymap.set('x', '/', '<Plug>(comment_toggle_linewise_visual)')

-- Window navigation: Ctrl+Shift + h/j/k/l
vim.keymap.set('n', '<C-S-h>', '<C-w>h', { desc = 'Move to left window' })
vim.keymap.set('n', '<C-S-j>', '<C-w>j', { desc = 'Move to window below' })
vim.keymap.set('n', '<C-S-k>', '<C-w>k', { desc = 'Move to window above' })
vim.keymap.set('n', '<C-S-l>', '<C-w>l', { desc = 'Move to right window' })

-- Window creation: Ctrl+Shift + s/v
vim.keymap.set('n', '<C-S-s>', '<cmd>split<cr>',  { desc = 'Horizontal split' })
vim.keymap.set('n', '<C-S-w>', '<cmd>vsplit<cr>', { desc = 'Vertical split' })

-- Close window: Ctrl+Shift + q
vim.keymap.set('n', '<C-S-q>', '<C-w>q', { desc = 'Close window' })

-- Resize windows: Ctrl+Shift + arrows
vim.keymap.set('n', '<C-S-Up>',    '<cmd>resize +2<cr>',          { desc = 'Increase window height' })
vim.keymap.set('n', '<C-S-Down>',  '<cmd>resize -2<cr>',          { desc = 'Decrease window height' })
vim.keymap.set('n', '<C-S-Right>', '<cmd>vertical resize +2<cr>', { desc = 'Increase window width' })
vim.keymap.set('n', '<C-S-Left>',  '<cmd>vertical resize -2<cr>', { desc = 'Decrease window width' })
