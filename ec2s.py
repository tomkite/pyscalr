#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

header = 'instance_id|name|org|owner|role|status|image_id|instance_type|state|vpc_id|subnet_id|architecture|ebs_optimized|elastic_gpu_associations|hypervisor|iam_instance_profile|id|image|instance_lifecycle|kernel_id|key_name|key_pair|launch_time|monitoring|network_interfaces|placement|placement_group|platform|private_ip_address|public_ip_address|root_device_name|root_device_type|security_groups|spot_instance_request_id|state_reason|subnet|tags|virtualization_type|volumes|vpc|vpc_addresses'
print(header)

ec2 = boto3.resource('ec2', region_name='ap-northeast-2')
filters = [{'Name':'tag:Name', 'Values':['Scalr-dev', '*scalr*']}]

#for h in ec2.instances.filter(Filters=filters):
for h in ec2.instances.all():
    tag_vals = [t['Value'] for t in h.tags if t['Key'] in 'Name,owner,organization,role'.split(',')]

    name = [t['Value'] for t in h.tags if t['Key'] in ['Name', 'name']]
    org = [t['Value'] for t in h.tags if t['Key'] in ['Organization', 'organization']]
    owner = [t['Value'] for t in h.tags if t['Key'] in ['Owner', 'owner']]
    role = [t['Value'] for t in h.tags if t['Key'] in ['Role', 'role']]

    name = name[0] if name else None
    org = org[0] if org else None
    owner = owner[0] if owner else None
    role = role[0] if role else None

    state = [h.state[t] for t in h.state if t=='Name'][0]

    response = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(\
        h.instance_id,
        name,
        org,
        owner,
        role,
        state,
        h.image_id,
        h.instance_type,
        h.state,
        h.vpc_id,
        h.subnet_id,
        h.architecture,
        h.ebs_optimized,
        h.elastic_gpu_associations,
        h.hypervisor,
        h.iam_instance_profile,
        h.id,
        h.image,
        h.instance_lifecycle,
        h.kernel_id,
        h.key_name,
        h.key_pair,
        h.launch_time,
        h.monitoring,
        h.network_interfaces,
        h.placement,
        h.placement_group,
        h.platform,
        h.private_ip_address,
        h.public_ip_address,
        h.root_device_name,
        h.root_device_type,
        h.security_groups,
        h.spot_instance_request_id,
        h.state_reason,
        h.subnet,
        h.tags,
        h.virtualization_type,
        h.volumes,
        h.vpc,
        h.vpc_addresses)

    print(response)
