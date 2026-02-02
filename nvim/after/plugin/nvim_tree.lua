require("nvim-tree").setup()

vim.keymap.set("n", "<leader>t", "<cmd>NvimTreeToggle<CR>", { silent = true, desc = "Toggle NvimTree" })
vim.keymap.set("n", "<leader>r", "<cmd>NvimTreeFocus<CR>", { silent = true, desc = "Toggle NvimTree" })
