local ok_cmp, cmp = pcall(require, "cmp")
if not ok_cmp then return end

local ok_snip, luasnip = pcall(require, "luasnip")

cmp.setup({
    snippet = {
        expand = function(args)
            if ok_snip then luasnip.lsp_expand(args.body) end
        end,
    },

    completion = {
        autocomplete = {
            require("cmp.types").cmp.TriggerEvent.TextChanged,
            require("cmp.types").cmp.TriggerEvent.InsertEnter,
        },
        keyword_length = 0,
    },

    mapping = cmp.mapping.preset.insert({
        ["<C-Space>"] = cmp.mapping.complete(),
        ["<CR>"]      = cmp.mapping.confirm({ select = true }),
        ["<C-e>"]     = cmp.mapping.abort(),
        ["<Tab>"]     = cmp.mapping.select_next_item(),
        ["<S-Tab>"]   = cmp.mapping.select_prev_item(),
    }),

    sources = {
        { name = "nvim_lsp" },
        { name = "luasnip" },
    },
})

