require("hinski2.remap")
require("hinski2.set")
require("hinski2.lsp")

vim.api.nvim_create_autocmd("FileType", {
  pattern = "*",
  callback = function()
    vim.opt_local.formatoptions:remove({ "c", "r", "o" })
  end,
})
