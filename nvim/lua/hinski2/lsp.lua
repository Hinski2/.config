require("mason").setup()

local mason_lspconfig = require("mason-lspconfig")
mason_lspconfig.setup({
    ensure_installed = { "pyright", "lua_ls", "clangd", "rust_analyzer" },
    automatic_installation = true,
})

local on_attach = function(_, bufnr)
    local opts = { buffer = bufnr, silent = true, noremap = true }
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)         -- go to definition
    vim.keymap.set("n", "gr", vim.lsp.buf.references, opts)         -- go to reference
    vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)     -- rename
    vim.keymap.set("n", "<C-space>", vim.lsp.buf.code_action, opts) -- code action
    vim.keymap.set("n", "<Leader>a", vim.lsp.buf.hover, opts)       -- hower action
end

local servers = { "pyright", "lua_ls", "clangd", "rust_analyzer" }
for _, server in ipairs(servers) do
    vim.lsp.config[server] = {
        on_attach = on_attach,
    }
end

vim.lsp.config.rust_analyzer = {
  on_attach = function(c, b)
    on_attach(c, b)
    if vim.lsp.inlay_hint and vim.lsp.inlay_hint.enable then
      vim.lsp.inlay_hint.enable(true, { bufnr = b })
    end
  end,
  settings = {
    ["rust-analyzer"] = {
      inlayHints = {
        parameterHints = { enable = true },
        typeHints      = { enable = true },
        chainingHints  = { enable = true },
      },
    },
  },
}

vim.lsp.config.lua_ls = {
  on_attach = on_attach,
  settings = {
    Lua = {
      diagnostics = { globals = { "vim" } },
      workspace = { checkThirdParty = false },
      telemetry = { enable = false },
    },
  },
}

vim.lsp.enable(servers)

