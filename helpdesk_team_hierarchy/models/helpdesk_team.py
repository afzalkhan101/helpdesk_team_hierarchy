from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HelpdeskTeam(models.Model):
    _inherit = 'helpdesk.team'

    parent_id = fields.Many2one(
        'helpdesk.team',
        string='Parent Team',
        ondelete='restrict',
        index=True,
    )

    child_ids = fields.One2many(
        'helpdesk.team',
        'parent_id',
        string='Sub Teams',
    )

    team_members = fields.Many2many(
        'res.users',
        relation='helpdesk_team_members_rel',
        column1='team_id',
        column2='user_id',
        string='Team Members',
    )

    @api.constrains('parent_id')
    def _check_parent_id(self):
        for team in self:
            if not team.parent_id:
                continue
            if team.parent_id == team:
                raise ValidationError(
                    f"Team '{team.name}' cannot be its own parent."
                )
            if team._has_cycle():
                raise ValidationError(
                    f"Circular hierarchy detected for team '{team.name}'."
                )

    def _has_cycle(self):
        self.ensure_one()
        visited = set()
        node = self.parent_id
        while node:
            if node.id in visited or node.id == self.id:
                return True
            visited.add(node.id)
            node = node.parent_id
        return False
